<<<<<<< HEAD
from django.urls import path
from watch import views


urlpatterns = [
    path('api/business/',views.BusinessList.as_view())
=======
from django.urls import path,include
from . import views

urlpatterns = [
    path('posts/', views.showposts, name='posts'),
>>>>>>> 8b42fc756cdd53586df8844f3d316211bc29cb45
]