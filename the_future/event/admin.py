from django.contrib import admin

from .models import (
    PlayerEventTitle, PlayerEventValue, PlayerEventDirectory, Event
)


@admin.register(PlayerEventTitle)
class PlayerEventTitleAdmin(admin.ModelAdmin):
    pass


@admin.register(PlayerEventValue)
class PlayerEventValueAdmin(admin.ModelAdmin):
    pass


@admin.register(PlayerEventDirectory)
class PlayerEventDirectoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    pass