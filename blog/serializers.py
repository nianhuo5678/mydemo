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
        fields = ('author', 'author_name', 'article_title', 'article', 'content', 'pub_date')
        read_only_fields = ('pub_date',)

    def get_author_name(self, obj):
        return obj.author.__str__()

    def get_article_title(self, obj):
        return obj.article.__str__()


class ArticleSerializer(serializers.ModelSerializer):
    author_name = serializers.SerializerMethodField()
    # comments = CommentSerializer(many=True, source='comment_set')
    # 只返回本文作者对于本文的评论
    comments = CommentSerializer(many=True, source='get_comment_by_me')

    class Meta:
        model = Article
        fields = ('id', 'title', 'author', 'pub_date', 'author_name', 'content', 'comments')
        read_only_fields = ('author', 'pub_date')

    @staticmethod
    def get_author_name(obj):
        return obj.author.__str__()

    def create(self, validated_data):
        authenticated_id = self.context['request'].user.id  # 获取当前登录用户的id(auth_user表)
        validated_data['author'] = Author.objects.get(pk=authenticated_id)  # 通过id获取author对象
        article = Article.objects.create(**validated_data)
        return article



