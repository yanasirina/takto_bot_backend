from django.contrib import admin

from core import models


@admin.register(models.Course)
class Course(admin.ModelAdmin):
    list_display = ('name', 'is_active', )
    list_filter = ('is_active', )
    search_fields = ('name', )
