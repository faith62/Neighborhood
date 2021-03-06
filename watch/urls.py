from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.welcome, name='welcome'),
    path('homes/',views.home, name='home'),
    path('hood/<str:pk>',views.viewhood, name='singlehood'),
   
    path('new/post', views.new_post, name='new-post'),
    path('<username>/',views.UserProfile, name='profile'),
    path('profile/edit/', views.EditProfile, name='editprofile'),
    path('new/business', views.new_business, name='new-business'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
 