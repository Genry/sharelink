#coding: utf-8
from django.conf.urls import patterns, include, url
from journal.feed.views import FeedView


urlpatterns = patterns(
    '',
    url(r'^$', FeedView.as_view()),
)
