from django.conf.urls import url
from django.views.generic import ListView
from django.views.generic import DetailView

from blog.models import Post


urlpatterns = [
    url(r'^$', ListView.as_view(queryset=Post.objects.all().order_by('-date'),
                                template_name='blog/blog.html')),
    url(r'^(?P<slug>[\w-]+)/$', DetailView.as_view(model=Post, template_name='blog/post.html'), name='post'),
]
