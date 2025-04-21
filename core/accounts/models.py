from django.db import models
from django.contrib.auth.models import AbstractUser
from accounts.manager import UserManager
from django.contrib.auth import get_user_model


class ShopUser(AbstractUser):
    username = None
    email = models.EmailField(max_length=254, unique=True)
    profile_image = models.ImageField(upload_to="images/profile", null=True, blank=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='shopuser_set',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='shopuser_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def __str__(self):
        return self.email


class Address(models.Model):
    pin_code = models.CharField(max_length=7)
    local_address = models.CharField(max_length=255, null=True, blank=True)
    area_street_sector_village = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=50)
    town_city = models.CharField(max_length=255)
    Landmark = models.CharField(max_length=100, null=True, blank=True)
    is_default_address = models.BooleanField(default=False)


user = get_user_model()


class Customer(user):
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name="customer")
    is_primium = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=12)
    is_varified = models.BooleanField(default=False)
    is_seller = models.BooleanField(default=False)

    def __str__(self):
        return f"{super().first_name} {super().last_name}"
