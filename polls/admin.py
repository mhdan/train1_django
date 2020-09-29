from django.contrib import admin
from . import models


class ChoiceInline(admin.TabularInline):
    model = models.Choice
    extra = 1


@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'pub_date', 'was_published_recently')
    list_filter = ('pub_date',)
    # add search box with adding 'search_fields' to search on given field!!!
    search_fields = ['text']
    inlines = [ChoiceInline]


@admin.register(models.Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('text', 'vote', 'question')
    # we can use 'question__text' lookup for filter on others foreignkey fields!
    # changeing on what display for field by adding 'verbose_name=' in models defintion!!!
    list_filter = ('vote', 'question__text')
