import pyotp
from django.core.cache import cache


def generate_otp(user_id):
    secret = pyotp.random_base32()

    cache.set(f'otp_secret_{user_id}', secret, timeout=120)

    totp = pyotp.TOTP(secret)
    otp = totp.now()

    return otp

def verify_otp(user_id, otp):
    secret = cache.get(f'otp_secret_{user_id}')

    if secret is None:
        return False

    totp = pyotp.TOTP(secret)
    return totp.verify(otp)
