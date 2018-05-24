# -*- encoding: utf-8 -*-

from django.db import models
from django.utils import timezone


class Author(models.Model):
    name = models.TextField(max_length=30)
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
