from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Products(models.Model):
    # identifier = models.CharField(max_length=40, unique=True)
    USERNAME_FIELD = 'identifier'
    name = models.CharField(max_length=200)
    pic_ame = models.CharField(max_length=50)
    price = models.FloatField()

    def __str__(self):
        return self.name

    # class Meta(AbstractUser.Meta):
    #     pass
