from django.contrib import admin
from . import models


# with 'TabularInline' we can add and edit items in other foreignkey part at same time!
class BookInstanceInline(admin.TabularInline):
    model = models.BookInstance
    extra = 1   # number of default items


# same as TabularInline, but show same as Stack!
class BookInline(admin.StackedInline):
    model = models.Book
    extra = 1


@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'date_of_birth', 'date_of_death')
    list_filter = ('date_of_birth', 'date_of_death')
    # with 'fields' we can group the fields
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BookInline]


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    list_filter = ('title', 'author', 'genre')
    # the 'inlines' should be added to 1 model!!!(not many model)
    inlines = [BookInstanceInline]

    # with 'fieldsets' we can group fields with title for them
    fieldsets = (
        (None, {
            "fields": ('title', 'author'),
        }),
        ('Archive Info', {
            "fields": ('isbn',)
        }),
        ('About', {
            "fields": ('genre', 'summary')
        }),
    )


@admin.register(models.BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'status', 'due_back')
    list_filter = ('book', 'status', 'due_back')

    fieldsets = (
        (None, {
            "fields": ('book',)
        }),
        ('Archive Info', {
            "fields": ('id', 'imprint')
        }),
        ('Availability', {
            "fields": ('status', 'due_back')
        })
    )


@admin.register(models.Genre)
class GenreAdmin(admin.ModelAdmin):
    pass
