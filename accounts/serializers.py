from django.core.validators import RegexValidator
from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    phone_number = serializers.CharField(
        max_length=12,
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,12}$',
                message="Phone number must be entered in the format: '+999999999'. Up to 12 digits allowed."
            )
        ],
    )


class VerifyOTPRequestSerializer(serializers.Serializer):
    phone_number = serializers.CharField(
        max_length=12,
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,12}$',
                message="Phone number must be entered in the format: '+999999999'. Up to 12 digits allowed."
            )
        ],
    )
    otp = serializers.IntegerField(required=True)
