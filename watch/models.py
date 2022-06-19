from django.db import models
from django.contrib.auth.models import User

# Create your models here.
<<<<<<< HEAD

#business model
class Business(models.Model):
    bsn_name= models.CharField(max_length=100)
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null = True,)
    bsn_email= models.EmailField(max_length = 254)
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
        
=======
class Posts(models.Model):
    image = models.ImageField(upload_to = 'posts/',default='IMAGE')
    title =  models.CharField(max_length =30)
    description = models.TextField()
    

    def __str__(self):
        return self.title
>>>>>>> 8b42fc756cdd53586df8844f3d316211bc29cb45
