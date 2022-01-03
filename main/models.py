from django.db import models

# Create your models here.
class UserInfo(models.Model):
    username = models.CharField(unique=True,null=False,max_length=255)
    batch = models.IntegerField(null=True)
    skills = models.TextField()
