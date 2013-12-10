# Create your views here.
# -*- coding: utf-8 -*-
""" This file contains views for the cms app """

from django.shortcuts import render_to_response
from django.template import RequestContext

# models
from cms.models import Interview


def interview(request, slug):
    interview = Interview.objects.get(slug=slug)

    context = {
        "interview": interview,
    }

    template = 'interview.jade'

    return render_to_response(template, context,
                              context_instance=RequestContext(request))
