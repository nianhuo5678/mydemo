# -*- encoding: utf-8 -*-

from rest_framework import permissions


class ArticleDeleteUpdatePermissions(permissions.BasePermission):

    message = "Only author can delete/modify"

    """
    对象层权限检查。
    如果请求是GET, HEAD, OPTIONS之一，允许权限。
    规定只有作者才能删除、修改文章
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.id == obj.author.id


class CommentDeleteUpdatePermissions(permissions.BasePermission):

    """
    评论作者及评论所属文章的作者可以删除评论。
    评论发表后不能修改。
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.method in ('PUT', 'PATCH'):
            return False
        return request.user.id == obj.author.id or request.user.id == obj.article.author_id
