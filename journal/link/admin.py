#coding: utf-8
from django.contrib import admin
from journal.link.models import LinkFolder, Link


class LinkFolderAdmin(admin.ModelAdmin):
    """

    """
    list_display = ('name', 'order', )
    search_fields = ('name', )


class LinkAdmin(admin.ModelAdmin):
    """

    """
    list_display = ('name', 'order', 'link')
    search_fields = ('name', )


admin.site.register(LinkFolder, LinkFolderAdmin)
admin.site.register(Link, LinkAdmin)
