from  django.urls import include, path
from . import views

from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'boards', views.BoardViewSet)
router.register(r'lists', views.ListViewSet)
router.register(r'cards', views.CardViewSet)
router.register(r'comments', views.CommentViewSet)
router.register(r'attachments', views.AttachmentViewSet)
router.register(r'activitylogs', views.ActivityLogViewSet)
router.register(r'labels', views.LabelViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
