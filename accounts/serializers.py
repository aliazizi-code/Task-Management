from rest_framework import serializers


class OTPSerializer(serializers.Serializer):
    otp = serializers.CharField(required=True)
