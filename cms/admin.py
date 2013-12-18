from cms.models import Interview
from django.contrib import admin


class InterviewAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'link']

    def link(self, obj):
        url = "/%s" % obj.slug

        if obj.picture:
            return "<a href='%s' target='_blank'>Link</a>" % url
        return ""

    link.allow_tags = True
    link.short_description = 'Link'


admin.site.register(Interview, InterviewAdmin)
