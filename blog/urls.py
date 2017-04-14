from django.conf.urls import url

from . import views


urlpatterns = [
    # .com/blog/
    # url(r'^$', views.post_list, name='post_list'),
    url(r'^$', views.PostListView.as_view(), name='post_list'),

    # .com/blog/year/month/day/post-slug/
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$', views.post_detail, name='post_detail'),

    # .com/blog/post_id/share/
    url(r'^(?P<post_id>\d+)/share/$', views.post_share, name='post_share')
]