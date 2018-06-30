from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(r'authors', views.AuthorViewSet)
router.register(r'articles', views.ArticleViewSet, base_name='article')
router.register(r'comments', views.CommentViewSet)

