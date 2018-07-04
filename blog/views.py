# -*- encoding: utf-8 -*-
from permissions import ArticleDeleteUpdatePermissions
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

    # def get_queryset(self):
    #     # 只返回当前用户写的文章
    #     user_id = self.request.user.id
    #     return Article.objects.filter(author=Author.objects.get(pk=user_id))

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
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(
            author=Author.objects.get(pk=self.request.user.id)
        )

    def perform_destroy(self, instance):
        # 评论作者或文章作者可删除评论
        uid = self.request.user.id
        article_author_id = instance.article.author_id
        comment_author_id = instance.author_id
        if comment_author_id == uid or article_author_id == uid:
            instance.is_deleted = True
            instance.save()
            print(instance.__str__() + " deleted")
        else:
            raise Exception('Not authorized! \n'
                            'Only author of the comment or author of the article can delete the comment.')





