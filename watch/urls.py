from django.urls import path
from watch import views


urlpatterns = [
    path('api/business/',views.BusinessList.as_view())
]