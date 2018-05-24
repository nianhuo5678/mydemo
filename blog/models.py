# -*- encoding: utf-8 -*-

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Author(models.Model):
    user = models.ForeignKey(User) # 登录的用户名
    nickname = models.TextField(max_length=30, null=True)
    info = models.TextField(max_length=300, null=True)

    class Meta:
        ordering = ('id',)


class Article(models.Model):
    title = models.TextField(max_length=50)
    author = models.ForeignKey(Author)
    content = models.TextField(max_length=2000)
    pub_date = models.DateField(default=timezone.now)

    class Meta:
        ordering = ('id',)


class Comment(models.Model):
    author = models.ForeignKey(Author)
    article = models.ForeignKey(Article)
    content = models.TextField(max_length=500)
    pub_date = models.DateField(default=timezone.now)

    class Meta:
        ordering = ('id',)
