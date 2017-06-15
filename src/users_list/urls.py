from django.conf.urls import include, url
from django.contrib import admin
from .views import IndexView, UserDetailView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^user_detail/(?P<pk>\d+)/', UserDetailView.as_view(), name='detail')
    # url(r'article/(?P<id>[0-9]+)/$', post_detail, name='post_detail'),
]

