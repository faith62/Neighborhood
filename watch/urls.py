from django.urls import path
from watch import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('login/',views.loginuser,name='login'),
    path('signup/',views.signup,name='signup'),
    path('logout/',views.logoutuser,name='logout'),

    path('profile/<id>/',views.profile,name='user_profile'),
    path('profile_update/<str:username>/',views.profile_update,name='profile_update'),

    path('post-create/',views.post_create,name='post-create'),
    path('bus-create/',views.bussiness_create,name='bus-create'),

    path('amenity/police/',views.police,name='police'),
    path('amenity/hair&grooming/',views.hair_and_grooming,name='hair&grooming'),
    path('amenity/hospital/',views.hospital,name='hospital'),
    path('amenity/malls_and_markets/',views.malls_and_markets,name='malls_and_markets'),
    path('amenity/fastfood/',views.fastfood,name='fastfood'),

    path('hood/<hoodname>/',views.hood,name='hood-name'),

    path('reset_password/',auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"),name="reset_password"),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"),name="password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html"),name="password_reset_confirm"),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_done.html"),name="password_reset_complete"),
]