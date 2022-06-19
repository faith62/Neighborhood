from django.urls import path,include
from watch import views

urlpatterns = [
<<<<<<< HEAD
    path('api/business/',views.BusinessList.as_view())
    path('neighbourhood', views.neighborhood, name='neighborhood'),
    path('neighbourhood/<int:hood_id>', views.hood_details, name='hood_details'),
    path('add-hood', views.add_hood, name='add-hood'),
    path('join_hood/<id>', views.join_hood, name='join-hood'),
    path('leave_hood/<id>', views.leave_hood, name='leave-hood'),
=======
    path('',views.homepage,name='homepage'),
>>>>>>> 77ddcf0a47a3cf9930dd1e9c9a08ac05232b2c2d
]