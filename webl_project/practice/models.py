from django.db import models

# Create your models here.
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