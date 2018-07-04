# -*- encoding: utf-8 -*-

from rest_framework import permissions


class ArticleDeleteUpdatePermissions(permissions.BasePermission):

    message = "Only author can delete/modify this article"

    """
    对象层权限检查。
    如果请求是GET, HEAD, OPTIONS之一，允许权限。
    规定只有作者才能删除、修改文章
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.id == obj.author.id

