from django.db import models

# Create your models here.
class EasyUser(models.Model):
    name=models.CharField(max_length=255)
    friends=models.CharField(max_length=2550)