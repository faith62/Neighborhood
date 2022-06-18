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

    @classmethod
    def update_neighborhood(cls, id, name, location, population, description, police, health, education):
        cls.objects.filter(id=id).update(name=name, location=location, population=population, description=description,
                                         police=police, health=health, education=education)

    @classmethod
    def get_all_neighborhoods(cls):
        all_neighborhoods = cls.objects.all()
        return all_neighborhoods[::-1]

    @classmethod
    def get_neighborhood_by_name(cls, name):
        return cls.objects.filter(name=name)

    @classmethod
    def get_neighborhood_by_location(cls, location):
        return cls.objects.filter(location=location)

    @classmethod
    def get_neighborhood_by_population(cls, population):
        return cls.objects.filter(population=population)

    @classmethod
    def get_neighborhood_by_description(cls, description):
        return cls.objects.filter(description=description)

    @classmethod
    def get_neighborhood_by_police(cls, police):
        return cls.objects.filter(police=police)