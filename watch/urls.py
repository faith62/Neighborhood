from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.home, name='home'),
    path('hood/<str:pk>',views.viewhood, name='singlehood'),
    path('new/post', views.new_post, name='new-post'),
    path('<username>/',views.UserProfile, name='profile'),
    path('profile/edit/', views.EditProfile, name='editprofile'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
 