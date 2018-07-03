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
            'gender'
        )


class CommentSerializer(serializers.ModelSerializer):
    author_name = serializers.SerializerMethodField()
    article_title = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ('author', 'author_name', 'article_title', 'article', 'id', 'is_deleted', 'content', 'pub_date')
        read_only_fields = ('author', 'pub_date', 'is_deleted')

    def get_author_name(self, obj):
        return obj.author.__str__()

    def get_article_title(self, obj):
        return obj.article.__str__()


class ArticleSerializer(serializers.ModelSerializer):
    author_name = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True, source='comment_set', read_only=True)
    # 只返回本文作者对于本文的评论
    # comments = CommentSerializer(many=True, source='get_comment_by_me')

    class Meta:
        model = Article
        fields = ('id', 'title', 'author', 'pub_date', 'is_deleted', 'author_name', 'content', 'comments')
        read_only_fields = ('author', 'pub_date', 'is_deleted')

    @staticmethod
    def get_author_name(obj):
        return obj.author.__str__()
