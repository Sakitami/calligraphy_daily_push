"""calligraphy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import to include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from daily_push.views import ArticleByDateAPIView, ArticleByIdAPIView, search_articles, search_knowledge
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('by_date/<date>/', ArticleByDateAPIView.as_view(), name='article_by_date'),
    path('by_id/<article_id>/', ArticleByIdAPIView.as_view(), name='article_by_id'),
    path('search/daily/', search_articles, name='search_articles'),
    path('search/knowledge/', search_knowledge, name='search_articles'),
    path('docs/', include_docs_urls(title='Calligraphy API'))
]
