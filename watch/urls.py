from django.urls import path,include
from watch import views

urlpatterns = [
    path('',views.homepage,name='homepage'),

    path('post-create/',views.post_create,name='post-create'),

    path('amenity/police/',views.police,name='police'),
    path('amenity/hair&grooming/',views.hair_and_grooming,name='hair&grooming'),
    path('amenity/hospital/',views.hospital,name='hospital'),
    path('amenity/malls_and_markets/',views.malls_and_markets,name='malls_and_markets'),
    path('amenity/fastfood/',views.fastfood,name='fastfood'),
]