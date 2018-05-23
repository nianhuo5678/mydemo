# -*- encoding: utf-8 -*-
from rest_framework import serializers
from models import Author, Article, Comment


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = (
            'name',
            'info',
        )


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = (
            'title',
            'author',
            'content',
            'pub_date',
        )


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            'author',
            'article',
            'content',
            'pub_date',
        )
