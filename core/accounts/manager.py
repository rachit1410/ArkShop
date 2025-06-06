from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('email number is required')

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('superuser must have is_superuser True')

        if extra_fields.get('is_staff') is not True:
            raise ValueError('staff must have is_staff True')

        if extra_fields.get('is_active') is not True:
            raise ValueError('active must have is_active True')

        return self.create_user(email, password, **extra_fields)
