from django.contrib import admin
from django.urls import path, include
from . import views as practice_views
urlpatterns = [
    path('', practice_views.problems, name='practice-problems'),
    path('<str:pk>', practice_views.oneProblem, name='practice-oneproblem'),
    #path('file/upload/', practice_views.uploadFile, name='practice-upload')
]
