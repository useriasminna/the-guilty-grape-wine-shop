"""
Users App - Models
----------------
Models for Users App.
"""
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,\
                                       PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    def create_user(self, email, password=None, is_active=True, is_staff=False,
                    is_admin=False, **extra_fields):
        """Define method for creating user"""
        if not email:
            raise ValueError("Users must have an email address")
        if not password:
            raise ValueError("Users must have a password")
        user = self.model(
            email=self.normalize_email(email),
            **extra_fields
        )

        user.set_password(password)
        user.is_staff = is_staff
        user.is_admin = is_admin
        user.is_active = is_active
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password,  **extra_fields):
        """Define method for creating superuser"""
        user = self.create_user(
            email=email,
            password=password,
            is_admin=True,
            is_staff=True,
            **extra_fields

        )
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Define a custom User Model"""
    email = models.EmailField(verbose_name='email address', unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    @property
    def is_superuser(self):
        """Return User Superuser state"""
        return self.is_admin

    def has_perm(self, *args):
        """Returns true if user has permisions"""
        return self.is_staff

    def has_module_perms(self, *args):
        """Returns true if user has module permisions"""
        return self.is_staff

    def __str__(self):
        """Override str method"""
        return str(self.email)
