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
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSitemap


# consolidate sitemaps from all apps
sitemaps = {
    'posts': PostSitemap,
}

# includes a url() that forwards requests with the pattern app/ to the module app.urls
# (the file with the relative URL /app/urls.py
urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # .com/
    url(r'^', include('home.urls')),

    # .com/about/
    url(r'^about/', include('about.urls')),

    # .com/account/
    url(r'^account/', include('account.urls')),

    # .com/blog/
    url(r'^blog/', include('blog.urls', namespace='blog', app_name='blog')),

    # .com/contact/
    url(r'^contact/', include('contact.urls')),
    url(r'^news/', include('news.urls')),
    url(r'^polls/', include('polls.urls')),

    # sitemap for webcrawlers
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]

