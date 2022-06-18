from rest_framework import serializers
from .models import business

class businessSerializer(serializers.ModelSerializer):
    class Meta:
        model = business
        fields= ('business_name','business_email', 'user')