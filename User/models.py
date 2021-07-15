from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(models.Model):
    # identifier = models.CharField(max_length=40, unique=True)
    USERNAME_FIELD = 'identifier'
    user_name = models.CharField(max_length=300)
    password = models.CharField(max_length=300)
    yue = models.FloatField()

    def __str__(self):
        return self.username
    
    # class Meta(AbstractUser.Meta):
    #     pass