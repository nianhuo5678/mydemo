# -*- encoding: utf-8 -*-
from rest_framework import serializers
from models import User, Article, Comment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'password',
            'is_admin',
            'info',
        )


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = (
            'title',
            'user',
            'content',
            'pub_date',
        )


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            'user',
            'article',
            'content',
            'pub_date',
        )
