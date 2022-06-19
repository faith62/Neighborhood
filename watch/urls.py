from django.urls import path,include
from watch import views

urlpatterns = [
    path('',views.homepage,name='homepage'),
]