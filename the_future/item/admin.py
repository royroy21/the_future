from django.contrib import admin

from .models import BattleItem, StandardItem


@admin.register(BattleItem)
class BattleItemAdmin(admin.ModelAdmin):
    pass


@admin.register(StandardItem)
class StandardItemAdmin(admin.ModelAdmin):
    pass