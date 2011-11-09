'''
Created on 17.10.2011

@author: xaralis
'''
from django.conf.urls.defaults import patterns, url

from ella.articles.models import Article
from ella.core.custom_urls import resolver

from .views import article_detail, article_page

# List this only to enable inclusion from base urls.py DO NOT DELETE
urlpatterns = patterns('iw.iwapp.views',)

browse_article_patterns = patterns('iw.iwapps.views',
    url(r'^strana/(?P<page>\d+)/$', article_page, name="article_page")
)

resolver.register(browse_article_patterns, model=Article)
resolver.register_custom_detail(Article, article_detail)
