from django.http import Http404
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import Article
from .serializers import ArticleSerializer

from django.utils import timezone


# Create your views here.
class ArticleByDateAPIView(APIView):
    """
    通过日期获取文章全部信息
    """
    def get_object(self, date):
        try:
            return Article.objects.get(date=date)
        except Article.DoesNotExist:
            raise Http404

    def get(self, request, date):
        article = self.get_object(date)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)


class ArticleByIdAPIView(APIView):
    """
    通过文章id获取文章全部信息
    """
    def get_object(self, article_id):
        try:
            return Article.objects.get(id=article_id)
        except Article.DoesNotExist:
            raise Http404

    def get(self, request, article_id):
        article = self.get_object(article_id)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

@api_view(['GET'])
def search_articles(request):
    """
    通过关键字搜索文章
    """
    keyword = request.query_params.get('keyword')
    if not keyword:
        return Response({'error': 'keyword is required'}, status=status.HTTP_400_BAD_REQUEST)
    keyword = request.GET.get('keyword')
    articles = Article.objects.filter(title__contains=keyword)
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)