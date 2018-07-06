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


class ParentNodeRelatedField(serializers.PrimaryKeyRelatedField):
    """
    筛选可回复的评论：同一篇文章的所有评论（包括自己的评论）。
    """
    def get_queryset(self):
        article = self.context.get('view').kwargs.get('article')
        return Comment.objects.filter(article=article)


class CommentSerializer(serializers.ModelSerializer):
    author_name = serializers.SerializerMethodField()
    article_title = serializers.SerializerMethodField()
    # parent = ParentNodeRelatedField(required=False, allow_null=True)

    class Meta:
        model = Comment
        fields = (
            'author', 'author_name', 'article_title', 'article', 'id', 'is_deleted', 'content', 'pub_date', 'parent'
        )
        read_only_fields = ('author', 'pub_date', 'is_deleted')

    @staticmethod
    def get_author_name(obj):
        return obj.author.__str__()

    @staticmethod
    def get_article_title(obj):
        return obj.article.__str__()


class ArticleSerializer(serializers.ModelSerializer):
    author_name = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        fields = ('id', 'title', 'author', 'pub_date', 'is_deleted', 'author_name', 'content', 'comments')
        read_only_fields = ('author', 'pub_date', 'is_deleted')

    @staticmethod
    def get_author_name(obj):
        return obj.author.__str__()
