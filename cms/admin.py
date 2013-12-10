from cms.models import Interview
from django.contrib import admin


class InterviewAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']


admin.site.register(Interview, InterviewAdmin)
