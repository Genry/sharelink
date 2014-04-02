from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^djangojs/', include('djangojs.urls')),
    url(r'^$', include('journal.feed.urls')),

    url(r'^grappelli/', include('grappelli.urls')),  # grappelli URLS

    url(r'^design/(?P<template_name>[^/]+)', 'journal.base.views.render_template'),
)
