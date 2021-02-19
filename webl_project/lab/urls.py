from django.contrib import admin
from django.urls import path, include
from . import views as lab_views
urlpatterns = [
    path('', lab_views.labProblems, name='lab-labproblems'),
    path('<str:pk>', lab_views.labOneProblem, name='lab-labproblemone'),
    path('assignments/all', lab_views.labAssignments, name='lab-labassignments'),
    path('assignments/all/<str:pk>', lab_views.oneAssignment, name='lab-oneassignment')
]
