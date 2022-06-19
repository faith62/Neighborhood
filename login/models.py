from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager
from django.db.models.deletion import CASCADE
# from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.db import models
from PIL import Image
from django.conf import settings

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if email is None:
            raise ValueError('Users must have an email')

        user=self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,email, password=None):
        if password is None:
            raise ValueError('Password should not be none')

        user=self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.save()
        return user
        

class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255)
    email = models.EmailField(('email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.username


