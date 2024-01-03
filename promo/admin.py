from django.contrib import admin

from promo import models


@admin.register(models.PromoCode)
class PromoCodeAdmin(admin.ModelAdmin):
    list_display = ('name', 'student', 'description', 'is_active')
    search_fields = ('name',)
    list_filter = ('is_active',)
