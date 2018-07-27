from django.db import models
from list import constant

# Create your models here.
class Task_models (models.Model):
    title = models.CharField(max_length= 200)
    description = models.TextField(null = True,blank = True)
    completiondate = models.DateTimeField()
    priority = models.CharField(max_length= 100,choices = constant.task_priority)
    iscompleted = models.BooleanField(default = False )

    def __str__(self):
        return self.title