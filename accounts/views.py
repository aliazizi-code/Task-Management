from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User
from .otp import generate_otp, verify_otp, delete_otp
from .serializers import UserSerializer, VerifyOTPRequestSerializer


class GenerateOTPView(APIView):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            data = serializer.validated_data
            user, created = User.objects.get_or_create(phone_number=data['phone_number'])

            otp = generate_otp(user.id)

            print(f'Your OTP is: {otp}')

            return Response(
                data={'message': 'OTP sent successfully'},
                status=status.HTTP_200_OK if not created else status.HTTP_201_CREATED
            )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyOTPView(APIView):
    serializer_class = VerifyOTPRequestSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            data = serializer.validated_data
            user = get_object_or_404(User, phone_number=data['phone_number'])
            print(user)

            if verify_otp(user.id, data['otp']):
                delete_otp(user.id)
                return Response(data=self._handle_login(data['phone_number']), status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_401_UNAUTHORIZED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def _handle_login(self, phone_number):
        user = User.objects.filter(phone_number=phone_number).first()

        if user is None:
            user = User(phone_number=phone_number)
            user.save()
            created = True
        else:
            created = False

        refresh = RefreshToken.for_user(user)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'created': created
        }
