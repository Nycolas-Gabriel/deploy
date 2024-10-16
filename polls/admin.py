from django.contrib import admin

from .models import Choice, Question


@admin.register(Question)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    pass
