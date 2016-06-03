"""fx_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.contrib import admin
from article import views
from article.views import RSSFeed


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name="home"),
    url(r'^about/$', views.about,name="about"),
    url(r'^message/$', views.message,name="message"),
    url(r'^archive/$', views.archive,name="archive"),
    url(r'^feed/$', RSSFeed(), name = "RSS"),  
    url(r'^search/$', views.blog_search, name = "search"),
    url(r'^article/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<id>\d+)/$', views.detail, name="detail"),
    url(r'^article/(?P<year>\d{4})/(?P<month>\d{1,2})/$', views.archive_month,name="archive_month"),
    url(r'^articleClassfi/(?P<classfi>\w+)/$', views.classfiDetail, name="classfiDetail"),
    url(r'^articleTag/(?P<tag>\w+)/$', views.tagDetail, name="tagDetail"),

]
