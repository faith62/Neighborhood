from email import message
from django.shortcuts import render
from django.http import Http404

from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Business

from .serializer import BusinessSerializer
from rest_framework import status

# Create your views here.
class BusinessList(APIView):
    def get(self, request, format=None):
        all_business = Business.objects.all()
        serializers = BusinessSerializer(all_business, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = BusinessSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def business(request):
        business =Business.objects.all()
        
        return render(request,'', {'business':business})

    def search_business(request):
        if 'business' in request.GET and request.GET["business"]:
            business_name = request.GET.get("business")
            searched_business = Business.find_business(business_name)
            message = f"{business_name}"

            return render(request, '',{"message":message,"businesses": searched_business})

        else:
            message = "You haven't searched for any term"
            return render(request, '',{"message":message})