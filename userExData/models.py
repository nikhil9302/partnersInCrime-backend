from django.db import models

# Create your models here.
class UserData(models.Model):
    username = models.TextField()
    actualName = models.TextField()
    bio = models.TextField(blank = True)
    batch = models.PositiveIntegerField(blank = True)
    email = models.EmailField(max_length = 254)
    skills = models.TextField()
    contactNum = models.BigIntegerField(blank = True)
    createdAt = models.DateTimeField(auto_now_add = True)
    
    # social links
    github = models.URLField(blank = True)
    
    def __str__(self):
        return self.username
    