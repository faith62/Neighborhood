from django.db import models
from django.contrib.auth.models import User
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

    @classmethod
    def update_neighbourhood(cls, id, name, location, population, description, police, health, education):
        cls.objects.filter(id=id).update(name=name, location=location, population=population, description=description,
                                         police=police, health=health, education=education)

    @classmethod
    def get_all_neighbourhoods(cls):
        all_neighbourhoods = cls.objects.all()
        return all_neighbourhoods[::-1]

    @classmethod
    def get_neighbourhood_by_name(cls, name):
        return cls.objects.filter(name=name)

    @classmethod
    def get_neighbourhood_by_location(cls, location):
        return cls.objects.filter(location=location)

    @classmethod
    def get_neighbourhood_by_population(cls, population):
        return cls.objects.filter(population=population)

    @classmethod
    def get_neighbourhood_by_description(cls, description):
        return cls.objects.filter(description=description)

    @classmethod
    def get_neighbourhood_by_police(cls, police):
        return cls.objects.filter(police=police)


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
        