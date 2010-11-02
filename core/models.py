from django.db import models

# Create your models here.
class Conference(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
