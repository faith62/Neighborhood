from django.db import models
from Cloudinary.models import CloudField


class Neighbourhood(models.Model):
    """
    Neighbourhood class to define the neighbourhoods present
    """
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    population = models.IntegerField()
    admin = models.ForeignKey("UserProfile", on_delete=models.CASCADE, related_name='hood',default=none,null=true)
    description = models.TextField()
    police = models.IntegerField()
    health = models.IntegerField()
    education = models.IntegerField()
    hood_logo = CloudinaryField('image')
    def __str__(self):
        return self.save()
    def create_neighbourhood(self):
        return self.save()
    def delete_neighbourhood(self):
        return self.delete()

    @classmethod
    def find_neighbourhood(cls,neighbourhood_id):
        return cls.objects.filter(id=neighbourhood_id)