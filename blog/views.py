# -*- encoding: utf-8 -*-
from rest_framework import viewsets
from models import Author, Article, Comment
from serializers import AuthorSerializer, ArticleSerializer, CommentSerializer


# 单独要求一个接口需要登录
# @permission_classes((IsAuthenticated,))
class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer

    def get_queryset(self):
        user_id = self.request.user.id
        return Article.objects.filter(author=Author.objects.get(pk=user_id))

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()
        print(instance.__str__() + " deleted")


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()
        print(instance.__str__() + " deleted")




