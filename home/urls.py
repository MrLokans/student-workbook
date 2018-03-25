from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.main_page),
    path('oauth/', include('social_django.urls', namespace='social')),
    path('login/', auth_views.login, name='login'),
    path('logout/', auth_views.logout, name='logout'),
    path('registration/', views.registration, name='registration'),
]
