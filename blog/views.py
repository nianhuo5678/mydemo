# -*- encoding: utf-8 -*-
from rest_framework import viewsets
from models import Author, Article, Comment
from serializers import AuthorSerializer, ArticleSerializer, CommentSerializer
from django.contrib.auth import authenticate, login
from django.http import HttpResponse


# Create your views here.
class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
