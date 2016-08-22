from django.contrib import admin

from .models import (
    ArmArmour, BackPack, BodyArmour, Faction, Player, LegArmour)


@admin.register(ArmArmour)
class ArmArmourAdmin(admin.ModelAdmin):
    pass


@admin.register(LegArmour)
class LegArmouradmin(admin.ModelAdmin):
    pass


@admin.register(BodyArmour)
class BodyArmourAdmin(admin.ModelAdmin):
    pass


@admin.register(BackPack)
class BackPackAdmin(admin.ModelAdmin):
    pass


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    pass


@admin.register(Faction)
class FactionAdmin(admin.ModelAdmin):
    pass