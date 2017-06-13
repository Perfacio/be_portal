from django.conf.urls import include, url
from django.contrib import admin
from .views import index_page, post_detail

urlpatterns = [
    url(r'^$', index_page, name='index'),
    url(r'article/(?P<id>[0-9]+)/$', post_detail, name='post_detail'),
]

