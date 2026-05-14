import random
from django.core.mail import send_mail
from django.conf import settings

def send_otp_email(user):
    """Send a 6-digit OTP to the user's registered email address."""
    otp = str(random.randint(100000, 999999))

    send_mail(
        subject='Password Reset OTP',
        message=f'Your OTP is: {otp}. It will expire in 10 minutes.',
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[user.email],
    )

    return otp