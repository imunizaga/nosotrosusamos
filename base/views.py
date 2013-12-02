# -*- coding: utf-8 -*-
""" This file contains some generic purpouse views """

from django.shortcuts import render_to_response
from django.template import RequestContext


def index(request):
    """ view that renders a default home"""
    return render_to_response('index.jade',
                              context_instance=RequestContext(request))
