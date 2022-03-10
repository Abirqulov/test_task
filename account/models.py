from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    password1 = models.CharField(max_length=120)
    password2 = models.CharField(max_length=120)

    def __str__(self):
        return self.username
