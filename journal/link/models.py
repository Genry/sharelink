#coding: utf-8
from django.contrib.auth import get_user_model
from django.db import models
from journal.base.models import BaseAbstractModel

from taggit.managers import TaggableManager

User = get_user_model()


class LinkFolder(BaseAbstractModel):
    """
    links folder
    """
    name = models.TextField(max_length=50, blank=True)
    order = models.PositiveIntegerField(default=0)

    def __unicode__(self):
        return self.name


class Link(LinkFolder):
    """
    model for links
    """
    user = models.ForeignKey(User, null=True)
    url = models.TextField(max_length=500, null=True, blank=True)
    folder = models.ForeignKey(LinkFolder, null=True, blank=True, related_name="links")
    rating = models.PositiveIntegerField(default=0)

    tags = TaggableManager(blank=True)

    def __unicode__(self):
        return self.name