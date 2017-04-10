from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

from . import views

#app_name = 'accounts'


urlpatterns = [
    # .com/accounts/
    url(r'^$', views.AccountView.as_view(), name='display_account'),

    # .com/accounts/login
    url(r'^login/$', auth_views.login, {'template_name': 'accounts/login.html',
                                        'redirect_authenticated_user': True}, name='login'),

    # .com/accounts/logout
    url(r'^logout/$', auth_views.logout, {'template_name': 'accounts/logged_out.html'}, name='logout'),

    # .com/accounts/signup
    url(r'^signup/$', views.signup, name='signup'),

    # .com/accounts/update
    url(r'^update/$', views.AccountUpdate.as_view(), name='update_account'),

    # .com/accounts/oauth
    url(r'^oauth/', include('social_django.urls', namespace='social')),

    # .com/accounts/settings
    url(r'^settings/$', views.settings, name='settings'),

    # .com/accounts/settings/password
    url(r'^settings/password/$', views.password, name='password'),
]


