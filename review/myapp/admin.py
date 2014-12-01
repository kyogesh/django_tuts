from django.contrib import admin

from .models import Poll, Choice, PollUser, Vote


class ChoiceTabularInline(admin.TabularInline):

    model = Choice
    extras = 3


class PollAdmin(admin.ModelAdmin):

    list_display = ['question', 'pub_date', 'was_published_recently']
    fieldsets = [
        (None, {'fields': ['question']}),
        ('Date Published', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    search_fields = ['question']
    inlines = [ChoiceTabularInline]


class ChoiceAdmin(admin.ModelAdmin):

    list_display = ['choice', 'votes']

admin.site.register(Poll, PollAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(PollUser)
admin.site.register(Vote)
