from django.db import models
from users.models import CustomUser
# Create your models here.
#class LabClass(models.Model):
#    lab_name = models.CharField(max_length=100, default='Programming Lab')
#    users = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#
#    def __str__(self):
#        return self.lab_name

class LabProblems(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    objective = models.TextField()
    task = models.TextField(default='')
    input_content = models.TextField()
    output_content = models.TextField()

    def __str__(self):
        return self.title

class Assignments(models.Model):
    title = models.CharField(max_length=150, default='')
    description = models.TextField(default='')
    objective = models.TextField(default='')
    task = models.TextField(default='')
    input_content = models.TextField(default='')
    output_content = models.TextField(default='')
    status = models.BooleanField(default=False)
    

    def __str__(self):
        return self.title

class AssignmentSubmissions(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    problem = models.ForeignKey(Assignments, on_delete=models.CASCADE)
    code = models.FileField(upload_to='assignmentSubmissions/')
    approved = models.BooleanField(default=False)
    reviewed = models.BooleanField(default=False)
    teachers_remarks = models.TextField(default='')