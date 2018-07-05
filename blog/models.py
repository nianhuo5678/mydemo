# -*- encoding: utf-8 -*-

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from mptt.models import MPTTModel, TreeForeignKey
import const


class Author(models.Model):
    user = models.ForeignKey(User)  # 登录的用户名
    name = models.TextField(max_length=30, null=True)
    info = models.TextField(max_length=300, null=True)
    gender = models.IntegerField(
        null=True,
        choices=(
            (const.Gender.Male.value, 'Male'),
            (const.Gender.Female.value, 'Female')
        )
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('id',)


class Article(models.Model):
    title = models.TextField(max_length=50)
    author = models.ForeignKey(Author, related_name='articles')
    content = models.TextField(max_length=2000)
    pub_date = models.DateTimeField(default=timezone.now)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.title

    def get_comment_by_me(self):
        author_id = self.author_id
        article_id = self.id
        return Comment.objects.filter(author=author_id, article=article_id)


class Comment(MPTTModel):
    author = models.ForeignKey(Author)
    article = models.ForeignKey(Article, related_name='comments')
    content = models.TextField(max_length=500)
    pub_date = models.DateTimeField(default=timezone.now)
    is_deleted = models.BooleanField(default=False)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True, verbose_name='reply')

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.content
