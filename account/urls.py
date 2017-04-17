from django.conf.urls import url, include

from . import views


urlpatterns = [
    # .com/account/
    url(r'^$', views.dashboard, name='dashboard'),

    # .com/account/register/
    url(r'^register/$', views.register, name='register'),
    url(r'^edit/$', views.edit, name='edit'),

    # login / logout
    url(r'^', include('django.contrib.auth.urls')),
    #url(r'^logout/$', include('django.contrib.auth.views.logout'), name='logout'),
    #url(r'^logout-then-login/$', include('django.contrib.auth.views.logout_then_login'), name='logout_then_login'),


    # .com/account/login
    #url(r'^login/$', views.user_login, name='login'),
]
