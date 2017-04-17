from django.conf.urls import url, include

from . import views
from .feeds import LatestPostFeed


urlpatterns = [
    # .com/blog/
    url(r'^$', views.post_list, name='post_list'),
    # url(r'^$', views.PostListView.as_view(), name='post_list'),

    # .com/tag/tag_slug
    url(r'^tag/(?P<tag_slug>[-\w]+)/$', views.post_list, name='post_list_by_tag'),

    # .com/blog/year/month/day/post-slug/
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$', views.post_detail, name='post_detail'),

    # .com/blog/post_id/share/
    url(r'^(?P<post_id>\d+)/share/$', views.post_share, name='post_share'),

    # .com/blog/feed/
    url(r'^feed/$', LatestPostFeed(), name='post_feed'),

    # .com/blog/search
    url(r'^search/$', views.post_search, name='post_search'),
]