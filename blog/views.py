# -*- encoding: utf-8 -*-
from rest_framework import viewsets
from models import User, Article, Comment
from serializers import UserSerializer, ArticleSerializer, CommentSerializer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = ArticleSerializer