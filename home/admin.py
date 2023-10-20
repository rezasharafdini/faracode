from django.contrib import admin
from . import models


@admin.register(models.Portfolio)
class PortfilioAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'is_publish', 'show_image']
    search_fields = ('title',)
    list_editable = ('is_publish',)
    list_filter = ('is_publish',)
