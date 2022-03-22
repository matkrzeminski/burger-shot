from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from phonenumber_field.modelfields import PhoneNumberField

from .managers import CustomUserManager
from ..core.models import TimeStampedUUID
from ..locations.models import BaseAddress


class User(AbstractBaseUser, TimeStampedUUID, PermissionsMixin):
    email = models.EmailField("Email Address", unique=True)
    first_name = models.CharField("First Name", max_length=50)
    last_name = models.CharField("Last Name", max_length=50)
    phone_number = PhoneNumberField("Phone Number", max_length=30, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    @property
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"


class Address(BaseAddress):
    user = models.ForeignKey(
        User,
        related_name="addresses",
        related_query_name="address",
        on_delete=models.CASCADE,
    )
