from django.http import Http404
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.utils.serializer_helpers import ReturnList
from rest_framework import generics
from .models import Article, Knowledge
from .serializers import ArticleSerializer, KnowledgeSerializer

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
        return Response({'error': '关键字不能为空'})
    keyword = request.GET.get('keyword')
    articles = Article.objects.filter(title__contains=keyword)
    articles_content = Article.objects.filter(content__contains=keyword)
    serializer_content = ArticleSerializer(articles_content, many=True)
    serializer = ArticleSerializer(articles, many=True)
    
    return Response(ReturnList(serializer.data+serializer_content.data, serializer=serializer))

@api_view(['GET'])
def search_knowledge(request):
    """
    通过关键字搜索知识
    """
    keyword = request.query_params.get('keyword')
    if not keyword:
        return Response({'error': '关键字不能为空'})
    keyword = request.GET.get('keyword')
    articles = Knowledge.objects.filter(title__contains=keyword)
    articles_content = Knowledge.objects.filter(article__contains=keyword)
    serializer_content = KnowledgeSerializer(articles_content, many=True)
    serializer = KnowledgeSerializer(articles, many=True)
    
    return Response(ReturnList(serializer.data+serializer_content.data, serializer=serializer))