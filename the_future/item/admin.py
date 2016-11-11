from django.contrib import admin

from .models import (
    Armour,
    Ability,
    Item,
    Shield,
    Weapon,
)


@admin.register(Armour)
class ArmourAdmin(admin.ModelAdmin):
    pass


@admin.register(Ability)
class AbilityAdmin(admin.ModelAdmin):
    pass


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    pass


@admin.register(Shield)
class ShieldAdmin(admin.ModelAdmin):
    pass


@admin.register(Weapon)
class WeaponAdmin(admin.ModelAdmin):
    pass