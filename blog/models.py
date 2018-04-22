from django.db import models
from django.utils import timezone


# Create your models here.
class User(models.Model):
    username = models.TextField(max_length=30, blank=True, null=True)
    password = models.TextField(max_length=80, blank=True, null=True)

