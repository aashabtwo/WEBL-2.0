from django.db import models
from users.models import CustomUser
#from ..users.models import CustomUser
# the user models are needed for creating foreign key



# problem model
class Problems(models.Model):
    head = models.CharField(max_length=30, default='Lab One')
    title = models.CharField(max_length=150)
    description = models.TextField()
    objective = models.TextField()
    task = models.TextField(default='')
    input_content = models.TextField()
    output_content = models.TextField()

    def __str__(self):
        return self.title


class Submissions(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    problem = models.ForeignKey(Problems, on_delete=models.CASCADE)
    #title = models.TextField(max_length=100, default='Code')
    code = models.FileField(upload_to='uploads/')