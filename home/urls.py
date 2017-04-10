from django.conf.urls import url
from django.conf.urls import include
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^generic/$', views.generic, name='generic'),
    url(r'^elements/$', views.elements, name='elements'),
]
