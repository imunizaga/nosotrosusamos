from cms.models import Category
from cms.models import Interview
from cms.models import Tag
from django.contrib import admin


class InterviewAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'link', 'active']

    def link(self, obj):
        url = "/%s" % obj.slug

        if obj.picture:
            return "<a href='%s' target='_blank'>Link</a>" % url
        return ""

    link.allow_tags = True
    link.short_description = 'Link'


class TagAdmin(admin.ModelAdmin):
    list_display = ['title', 'link', 'categories_list']
    filter_horizontal = ['categories']

    def categories_list(self, obj):
        return ", ".join(obj.categories.all().values_list('title', flat=True))


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']

admin.site.register(Interview, InterviewAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
