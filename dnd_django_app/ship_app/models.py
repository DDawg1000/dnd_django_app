from django.db import models

# Create your models here.

class Button(models.Model):
    label = models.CharField(max_length=50)
    count = models.IntegerField(default=0)

