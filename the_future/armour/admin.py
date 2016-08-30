from django.contrib import admin

from .models import (
    ArmArmour, BackPack, BodyArmour, HeadArmour, LegArmour
)


@admin.register(ArmArmour)
class ArmArmourAdmin(admin.ModelAdmin):
    pass


@admin.register(LegArmour)
class LegArmouradmin(admin.ModelAdmin):
    pass


@admin.register(BodyArmour)
class BodyArmourAdmin(admin.ModelAdmin):
    pass


@admin.register(HeadArmour)
class HeadArmourAdmin(admin.ModelAdmin):
    pass


@admin.register(BackPack)
class BackPackAdmin(admin.ModelAdmin):
    pass