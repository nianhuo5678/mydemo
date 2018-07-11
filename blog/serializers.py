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
        article_id = self.context.get('view').kwargs.get('article_id')
        article = Article.objects.get(id=article_id)
        return Comment.objects.filter(article=article)


class CommentSerializer(serializers.ModelSerializer):
    author_name = serializers.SerializerMethodField()
    parent = ParentNodeRelatedField(required=False, allow_null=True)
    parents_list = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ('id', 'author_name', 'article', 'content', 'pub_date', 'parent', 'parents_list',)
        read_only_fields = ('author_name', 'pub_date', 'article', 'is_deleted', 'parents_list')

    def get_author_name(self, obj):
        return obj.author.__str__()

    def get_parents_list(self, obj):
        ancestors = obj.get_ancestors(include_self=True)
        ancestor_list = list()
        for ancestor in ancestors:
            ancestor_dict = dict()
            ancestor_dict['author'] = ancestor.author.name
            ancestor_dict['content'] = ancestor.content
            ancestor_list.append(ancestor_dict)
        return ancestor_list


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
