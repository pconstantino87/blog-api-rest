from django.db import models
from taggit.managers import TaggableManager

# Create your models here.


class Posts(models.Model):
    title = models.CharField(blank=False, max_length=100)
    subtitle = models.CharField(blank=False, max_length=100)
    content = models.TextField(blank=False)
    creator = models.ForeignKey(
        'auth.User', blank=True, null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = TaggableManager()

    def __str__(self):
        return self.title
