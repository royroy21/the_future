from django.contrib import admin

from .models import CombatRequest


@admin.register(CombatRequest)
class CombatRequestAdmin(admin.ModelAdmin):
    pass