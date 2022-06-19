from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from login.models import CustomUser
from django.conf import settings

# Create your models here
class Profile(models.Model):
    name = models.CharField(max_length=70)
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name= 'profile')
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
        
#business model
class Business(models.Model):
    CATEGORY = (
        ('Police Station','Police'),
        ('Hair&Grooming','Hair&Grooming'),
        ('Hospital','Hospital'),
        ('Mall&Markets','Mall&Markets'),
        ('Fast Foods','Fast Foods')
    )
    bsn_name= models.CharField(max_length=100)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,blank=True,null = True,)
    bsn_email= models.EmailField(max_length = 254)
    category = models.CharField(max_length=50, null=True, choices=CATEGORY)
    # neig_id = models.ForeignKey(Neighborhood, on_delete=models.CASCADE)

    def __str__(self):
        return self.bsn_name
   
    def create_business(self):
        self.save() 

    def delete_business(self):
        self.delete()  

    @classmethod
    def find_business(cls,business_name):
        businesses = cls.objects.filter(bsn_name__icontains=business_name).all()
        return businesses  

    def update_business(self):
        self.update()
        
class Posts(models.Model):
    image = models.ImageField(upload_to = 'posts/',default='IMAGE')
    title =  models.CharField(max_length =30)
    description = models.TextField()
    profile = models.ForeignKey(Profile,on_delete=models.SET_NULL, null=True)

    def save_post(self):
        '''Add Post to database'''
        self.save()

    def __str__(self):
        return self.title
