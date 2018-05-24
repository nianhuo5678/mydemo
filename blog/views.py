# -*- encoding: utf-8 -*-
from rest_framework import viewsets
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from models import Author, Article, Comment
from serializers import AuthorSerializer, ArticleSerializer, CommentSerializer


# 单独要求一个接口需要登录
# @permission_classes((IsAuthenticated,))
class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


