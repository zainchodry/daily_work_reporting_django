from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    ROLE_CHOICES = (
        ("ADMIN", "Admin"),
        ("MANAGER", "Manager"),
        ("EMPLOYEE", "Employee"),
    )

    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email


class Profile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile"
    )

    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    image = models.ImageField(
        upload_to="profiles/",
        blank=True,
        null=True
    )

    designation = models.CharField(
        max_length=100,
        blank=True
    )

    joining_date = models.DateField(
        auto_created=True,
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.user.email
    
class PasswordResetOtp(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    otp = models.CharField(max_length=6)
    created_At = models.DateTimeField(auto_now_add=True)