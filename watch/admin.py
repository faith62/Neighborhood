from django.contrib import admin
from .models import Business, Neighbourhood, Posts, Profile
# Register your models here.

admin.site.register(Posts)
admin.site.register(Profile)
admin.site.register(Business)
admin.site.register(Neighbourhood)