""" this document defines the project urls """

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    (r'^accounts/', include('users.urls')),
    url(r'^about/', 'cms.views.about', name='about'),
    url(r'^(?P<slug>\w+)/$', 'cms.views.interview', name='interview'),
    url(r'^$', 'base.views.index', name='home'),
)


if settings.DEBUG:
    urlpatterns += patterns('',
                           (r'^%s(?P<path>.*)$' % settings.MEDIA_URL[1:],
                            'django.views.static.serve', {
                                'document_root': settings.MEDIA_ROOT}))
