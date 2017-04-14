"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin


# includes a url() that forwards requests with the pattern app/ to the module app.urls
# (the file with the relative URL /app/urls.py
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('home.urls')),
    url(r'^about/', include('about.urls')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^blog/', include('blog.urls', namespace='blog', app_name='blog')),
    url(r'^contact/', include('contact.urls')),
    url(r'^news/', include('news.urls')),
    url(r'^polls/', include('polls.urls')),
]

