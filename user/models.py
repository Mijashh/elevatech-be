from typing import Any

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class UserRoles(models.TextChoices):
    STUDENT = 'student', 'Student'
    COMPANY = 'company', 'Company'

class CustomUserManager(BaseUserManager):
    def create_user(
        self, email, password=None, name=None, contact_no=None, role=UserRoles.STUDENT, **extra_fields
    ):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(
            email=email, 
            name=name, 
            contact_no=contact_no, 
            role=role,
            **extra_fields
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("role", UserRoles.STUDENT)  # Default role for superuser
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser):
    name = models.CharField(max_length=100, blank=True, null=True)
    contact_no = models.CharField(max_length=10, blank=True, null=True)
    email = models.EmailField(unique=True)
    role = models.CharField(
        max_length=20,
        choices=UserRoles.choices,
        default=UserRoles.STUDENT
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    objects = CustomUserManager()

    USERNAME_FIELD = "email"

    def __str__(self) -> Any:
        return self.email

    def has_perm(self, perm, obj=None) -> Any:
        return self.is_superuser

    def has_module_perms(self, app_label) -> Any:
        return self.is_superuser
