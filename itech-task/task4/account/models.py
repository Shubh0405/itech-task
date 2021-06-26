from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)
from phonenumber_field.modelfields import PhoneNumberField
from rest_framework_simplejwt.tokens import RefreshToken
# Create your models here.
class UserManager(BaseUserManager):

    def create_user(self, email, phone_number, password=None):
        if email is None:
            raise TypeError('Users should have a Email')

        user = self.model(email=self.normalize_email(email), phone_number=phone_number)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, phone_number, password):
        if password is None:
            raise TypeError('Password should not be none')

        user = self.create_user(email, phone_number)
        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    phone_number = PhoneNumberField()
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number']

    objects = UserManager()

    def __str__(self):
        return self.email

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return{
            'refresh':str(refresh),
            'access':str(refresh.access_token)
        }
