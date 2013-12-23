# -*- coding: utf-8 -*-
""" This file contains some generic purpouse views """

from django.shortcuts import render_to_response
from django.template import RequestContext
from cms.models import Interview


def index(request):
    """ view that renders a default home"""
    interviews = Interview.objects.filter(active=True).order_by("-created_at")

    grouped_interviews = []
    count = 0
    for interview in interviews:
        if count % 3 == 0:
            group = []
            grouped_interviews.append(group)

        group.append(interview)

        count += 1

    context = {
        "grouped_interviews": grouped_interviews,
        "interviews": interviews,
    }

    return render_to_response('index.jade', context,
                              context_instance=RequestContext(request))
