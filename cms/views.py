# Create your views here.
# -*- coding: utf-8 -*-
""" This file contains views for the cms app """

# django
from django.db.models import Count
from django.shortcuts import render_to_response
from django.template import RequestContext

# models
from cms.models import Category
from cms.models import Interview
from cms.models import Tag

# standard library
import json


def interview(request, slug):
    try:
        interview = Interview.objects.get(slug=slug)
    except Interview.DoesNotExist:
        return template_view(request, template=slug)

    interview.parse_tags(request=request)

    context = {
        "interview": interview,
    }

    template = 'interview.jade'

    return render_to_response(template, context,
                              context_instance=RequestContext(request))


def tags(request):
    categories = Category.objects.all().values('id', 'title')
    tags = Tag.objects.annotate(num_interviews=Count('interviews'))
    tags = tags.prefetch_related('categories')

    tag_data = []

    for tag in tags:
        tag_data.append({
            'title': tag.title,
            'num_interviews': tag.num_interviews,
            'categories': list(c.id for c in tag.categories.all(),),
        })

    context = {
        'tags': tags,
        'json_categories': json.dumps(list(categories)),
        'json_tags': json.dumps(tag_data),
    }

    template = 'tags.jade'

    return render_to_response(template, context,
                              context_instance=RequestContext(request))


def template_view(request, template):
    """ view that renders the about page"""

    context = {
        "interviews": Interview.objects.all(),
    }

    return render_to_response('{}.jade'.format(template), context,
                              context_instance=RequestContext(request))
