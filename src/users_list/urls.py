from django.conf.urls import include, url
from django.contrib import admin
from .views import IndexView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    # url(r'article/(?P<id>[0-9]+)/$', post_detail, name='post_detail'),
]

