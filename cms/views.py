# Create your views here.
# -*- coding: utf-8 -*-
""" This file contains views for the cms app """

from django.shortcuts import render_to_response
from django.template import RequestContext

# models
from cms.models import Interview


def interview(request, slug):
    try:
        interview = Interview.objects.get(slug=slug)
    except Interview.DoesNotExist:
        return template_view(request, template=slug)

    context = {
        "interview": interview,
    }

    template = 'interview.jade'

    return render_to_response(template, context,
                              context_instance=RequestContext(request))


def template_view(request, template):
    """ view that renders the about page"""

    context = {
        "interviews": Interview.objects.all(),
    }

    return render_to_response('{}.jade'.format(template), context,
                              context_instance=RequestContext(request))
