from django.contrib import admin
from .models import Neighbourhood,Business,Profile,Posts



# Register your models here.
admin.site.register(Neighbourhood)
admin.site.register(Profile)
admin.site.register(Business)
admin.site.register(Posts)