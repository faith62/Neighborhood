from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager
from django.db.models.deletion import CASCADE
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.db import models
from PIL import Image

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
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()


    def __str__(self):
        return self.username

class Profile(models.Model):
    name = models.CharField(max_length=70)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name= 'profile')
    bio = models.TextField(max_length=255)
    location = models.CharField(max_length=55)
    profile_photo = models.ImageField('image')
    # neighborhood = models.ForeignKey(Neighborhood, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self) -> str:
        return (self.user.username)

    def save_profile(self):
        super().user()

        img = Image.open(self.profile_photo.path)
        if img.height >300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.profile_photo.path)

    def delete_profile(self):
        self.delete()
