#coding: utf-8
from django.db import models


class BaseAbstractModel(models.Model):
    """
    base created modified model
    """
    created = models.DateTimeField(auto_now_add=True, null=True)
    modified = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True