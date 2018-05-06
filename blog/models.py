from django.db import models
from django.utils import timezone


# Create your models here.
class User(models.Model):
    username = models.TextField(max_length=30, blank=True, null=True)
    password = models.TextField(max_length=80, blank=True, null=True)
    is_admin = models.BooleanField(default=False)
    info = models.TextField(max_length=1200, null=True, blank=True)

