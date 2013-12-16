# -*- coding: utf-8 -*-
""" This file contains some generic purpouse views """

from django.shortcuts import render_to_response
from django.template import RequestContext
from cms.models import Interview


def index(request):
    """ view that renders a default home"""

    context = {
        "interviews": Interview.objects.all().order_by("-created_at")
    }

    return render_to_response('index.jade', context,
                              context_instance=RequestContext(request))
