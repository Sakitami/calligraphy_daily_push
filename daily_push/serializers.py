from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'image_url', 'classification', 'content', 'date', 'view', 'author', 'title']
