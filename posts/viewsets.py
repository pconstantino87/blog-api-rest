from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from .models import Posts
from .serializers import PostsSerializer, UpdatePostsSerializer

# Viewset


class PostsViewSet(viewsets.ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer


class UpdatePostsViewSet(viewsets.ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = UpdatePostsSerializer
    permission_classes = (IsAuthenticated,)
    http_method_names = ['patch', ]

    def update(self, request, pk=None, *args, **kwargs):
        user = request.user
        instance = self.get_object()
        data = {
            "title": request.POST.get('title', None),
        }
        serializer = self.serializer_class(instance=instance,
                                           data=data,  # or request.data
                                           context={'author': user},
                                           partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
