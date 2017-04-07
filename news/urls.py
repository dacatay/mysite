from django.conf.urls import url
from django.conf.urls import include
from django.views.generic import ListView
from django.views.generic import DetailView

from news.models import Post
from . import views


urlpatterns = [
    #url(r'^$', ListView.as_view(queryset=Post.objects.all().order_by('-date'),
    #                            template_name='news/news.html')),
    #url(r'^(?P<pk>\d+)$', DetailView.as_view(model=Post, template_name='news/post.html')),
    url(r'^$', views.news, name='name')
]
