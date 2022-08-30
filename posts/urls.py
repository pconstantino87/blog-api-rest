from django.urls import include, path
from rest_framework import routers

from . import viewsets as postsviewsets

router = routers.DefaultRouter()
router.register(r'posts', postsviewsets.PostsViewSet, 'Posts')
router.register(r'update-posts', postsviewsets.UpdatePostsViewSet,
                "update-posts")

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
