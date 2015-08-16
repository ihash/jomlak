"""jomlak URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from .views import FirstView, SalView
from django.views.decorators.csrf import csrf_exempt

from posts.views import MakePost, SubmitPost, PostListView, LikePostView, Bot

urlpatterns = [
    url(r'^search/', FirstView.as_view()),
    url(r'^sal/$', SalView.as_view()),
    url(r'^form/$', MakePost.as_view()),
    url(r'^post/', SubmitPost.as_view()),
    url(r'^postlist/$', PostListView.as_view()),
    url(r'^like/(?P<asha>\d+)/$', LikePostView.as_view()),
    url(r'^bot/$', csrf_exempt(Bot.as_view())),
]