# django
from django import template

# models
from cms.models import Interview

register = template.Library()


@register.tag(name='get_recent_interviews')
def recent_interviews(parser, token):
    """
    {% get_recent_interviews %}
    {{ recent_interviews }}
    """
    return MenuObject()


class MenuObject(template.Node):
    def __init__(self):
        pass

    def render(self, context):
        context['recent_interviews'] = Interview.objects.filter(
            active=True)[:5]
        return ''
