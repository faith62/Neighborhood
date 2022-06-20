from django.shortcuts import render
from .models import Neighbourhood,Profile,Posts,Business 

# Create your views here.
def home(request):
    
    homes = Neighbourhood.objects.all()

    return render(request, 'index.html',{'homes':homes,})