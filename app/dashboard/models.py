from django.db import models

# Create your models here.
class EasyUser(models.Model):
    name=models.CharField(max_length=255)
    real_name=models.CharField(max_length=255)
    friends=models.CharField(max_length=2550)
    goal_score=models.IntegerField(default=20)
    score=models.IntegerField(default=0)
    email=models.CharField(max_length=255)

