from rest_framework import exceptions, serializers
from taggit_serializer.serializers import (TaggitSerializer,
                                           TagListSerializerField)

from .models import Posts


class PostsSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()

    class Meta:
        model = Posts
        fields = "__all__"


class UpdatePostsSerializer(serializers.ModelSerializer):

    def validate(self, data):
        author = self.context['author']
        if "#" in data['title']:
            raise exceptions.ValidationError(detail="can not include '#' in title")  # NOQA
        return data

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.author = self.context['author']
        instance.save()
        return instance

    class Meta:
        model = Posts
        fields = '__all__'
