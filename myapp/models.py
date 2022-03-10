from django.db import models
from account.models import User
# Create your models here.


class Contact(models.Model):
    phone = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.phone


class Contact_Post(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    subject = models.CharField(max_length=255, null=True, blank=True)
    comment = models.TextField()

    def __str__(self):
        return self.name


class New(models.Model):
    user = models.ForeignKey(User, max_length=255, null=True, blank=True, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='images/news')
    title = models.CharField(max_length=255, null=True, blank=True)
    body = models.TextField(blank=True)

    def __str__(self):
        return self.title