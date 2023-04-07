from rest_framework import serializers
from .models import Article, Knowledge


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'image_url', 'classification', 'content', 'date', 'view', 'author', 'title']



class KnowledgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'date', 'classification', 'article', 'author', 'title']
