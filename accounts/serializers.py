from rest_framework import serializers

from accounts.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('phone_number',)


class VerifyOTPRequestSerializer(serializers.Serializer):
    phone_number = serializers.CharField(required=True)
    otp = serializers.IntegerField(required=True)
