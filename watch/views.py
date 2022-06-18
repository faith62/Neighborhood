from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from .models import  business
from .serializer import businessSerializer

# Create your views here.
class businessList(APIView):
    def get(self, request, format=None):
        all_merch = business.objects.all()
        serializers = businessSerializer(all_merch, many=True)
        return Response(serializers.data)