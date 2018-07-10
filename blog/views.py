# -*- encoding: utf-8 -*-
from permissions import ArticleDeleteUpdatePermissions, CommentDeleteUpdatePermissions
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
    queryset = Article.objects.all()
    permission_classes = (ArticleDeleteUpdatePermissions,)

    def perform_destroy(self, instance):
        # 标记删除文章
        instance.is_deleted = True
        instance.save()

    def perform_create(self, serializer):
        # 获取当前登陆用户作为文章作者
        serializer.save(
            author=Author.objects.get(pk=self.request.user.id)
        )


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.filter(is_deleted=False)
    serializer_class = CommentSerializer
    # permission_classes = (CommentDeleteUpdatePermissions,)

    def perform_create(self, serializer):
        serializer.save(
            author=Author.objects.get(pk=self.request.user.id)
        )

    def perform_destroy(self, instance):
        # 标记删除
        instance.is_deleted = True
        instance.save()





