from django.contrib import admin

from core import models


@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['telegram_id', 'username', 'name', 'phone_number']
    search_fields = ['telegram_id', 'username', 'name', 'phone_number']

from core import models


@admin.register(models.Course)
class Course(admin.ModelAdmin):
    list_display = ('name', 'is_active', )
    list_filter = ('is_active', )
    search_fields = ('name', )
