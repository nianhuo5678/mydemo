# -*- encoding: utf-8 -*-
from rest_framework import serializers
from models import Author, Article, Comment


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = (
            'user',
            'name',
            'info',
        )


class ArticleSerializer(serializers.ModelSerializer):
    author_name = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = ('id', 'title', 'author_name', 'content', 'pub_date')
        read_only_fields = ('author',)

    def get_author_name(self, obj):
        return obj.author.__str__()

    def create(self, validated_data):
        authenticated_id = self.context['request'].user.id  # 获取当前登录用户的id(auth_user表)
        validated_data['author'] = Author.objects.get(pk=authenticated_id)  # 通过id获取author对象
        article = Article.objects.create(**validated_data)
        return article


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            'author',
            'article',
            'content',
            'pub_date',
        )
