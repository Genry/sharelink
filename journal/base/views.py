#coding: utf-8
from django.shortcuts import render_to_response
from django.template import RequestContext


def render_template(request, template_name):
    """
    render design templates
    """
    if ".jade" not in template_name:
        template_name = "%s.jade" % template_name

    return render_to_response("design/%s" % template_name, {}, context_instance=RequestContext(request))
