from django.contrib import admin

from .models import Hero, Faction


@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    pass


@admin.register(Faction)
class FactionAdmin(admin.ModelAdmin):
    pass

