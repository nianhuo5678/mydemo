# coding=utf-8

from django.db import models
from django.utils import timezone


class User(models.Model):
    username = models.TextField(max_length=30, null=True)
    password = models.TextField(max_length=80, null=True)
    is_admin = models.BooleanField(default=False)
    info = models.TextField(max_length=300, null=True, blank=True)


class Article(models.Model):
    title = models.TextField(max_length=50)
    User = models.ForeignKey(User)
    content = models.TextField(max_length=2000)
    pub_date = models.DateField(default=timezone.now)


class Comment(models.Model):
    user = models.ForeignKey(User)
    article = models.ForeignKey(Article)
    content = models.TextField(max_length=500)
    pub_date = models.DateField(default=timezone.now)
