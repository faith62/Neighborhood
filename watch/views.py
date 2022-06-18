from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from .models import  business

from .serializer import businessSerializer
from rest_framework import status

# Create your views here.
class BusinessList(APIView):
    def get(self, request, format=None):
        all_business = business.objects.all()
        serializers = businessSerializer(all_business, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = businessSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)