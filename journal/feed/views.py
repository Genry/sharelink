#coding: utf-8
from django.views.generic import TemplateView


class FeedView(TemplateView):
    """

    """
    template_name = "feed/feed.jade"

    def get_context_data(self, **kwargs):
        return {"title": "linksaver"}
