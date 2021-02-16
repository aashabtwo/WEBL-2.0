from django.contrib import admin
from django.urls import path
from . import views as user_views
urlpatterns = [
    path('dashboard/', user_views.home, name='users-dashboard'),
    path('register/', user_views.register, name='users-register'),
    path('login/', user_views.loginUser, name='user-login'),
    path('logout/', user_views.logoutUser, name='user-logout'),
]
