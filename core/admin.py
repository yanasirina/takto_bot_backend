from django.contrib import admin

from core import models


@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['telegram_id', 'username', 'name', 'phone_number']
    search_fields = ['telegram_id', 'username', 'name', 'phone_number']

