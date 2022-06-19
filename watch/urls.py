from django.urls import path,include
from watch import views

urlpatterns = [
    path('api/business/',views.BusinessList.as_view()),
    path('neighbourhood', views.neighbourhood, name='neighbourhood'),
    path('neighbourhood/<int:hood_id>', views.hood_details, name='hood_details'),
    path('add-hood', views.add_hood, name='add-hood'),
    path('join_hood/<id>', views.join_hood, name='join-hood'),
    path('leave_hood/<id>', views.leave_hood, name='leave-hood'),
    path('',views.homepage,name='homepage'),
]