from django.contrib import admin
from django.urls import path, include
from . import views as lab_views
urlpatterns = [
    path('c/exp1', lab_views.theory, name='lab-exp1'),
    path('c/pick', lab_views.pick, name='lab-labpick'),
    path('c/lablist', lab_views.list, name='lab-lablist'),
    path('', lab_views.labProblems, name='lab-labproblems'),
    path('<str:pk>', lab_views.labOneProblem, name='lab-labproblemone'),
    path('assignments/all', lab_views.labAssignments, name='lab-labassignments'),
    path('assignments/all/<str:pk>', lab_views.oneAssignment, name='lab-oneassignment'),
    path('submissions/all', lab_views.submittedAssignments, name='lab-submissions'),
    path('submissions/all/<str:pk>', lab_views.oneSubmission, name='lab-onesubmission'),
    path('rejects/one/<str:pk>', lab_views.rejectedSubmissions, name='lab-rejects'),
    path('accepted/one/<str:pk>', lab_views.acceptedSubmissions, name='lab-accepted'),
]
