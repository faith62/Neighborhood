from django.urls import path
from django import views

urlpatterns = [
    path('api/business/',views.BusinessList.as_view())
]