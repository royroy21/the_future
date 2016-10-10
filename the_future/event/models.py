from django.db import models

from armour.models import (
    ArmArmour, BackPack, BodyArmour, HeadArmour, LegArmour
)
from item.models import BattleItem, ShieldItem
from utils.generic_models import CommonFields


class PlayerEventTitle(CommonFields):
    """
    For editors to create player event titles without having to worry
    about values
    """
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class PlayerEventValue(CommonFields):
    """
    Players are assigned modifiers for player events so that future
    events can reference
    """
    value = models.IntegerField()

    def __str__(self):
        return self.value


class PlayerEventDirectory(CommonFields):
    """
    Keep track of what player actions were performed against an event

    Saved either against players or events. If saved against players
    then modifiers are calculated.

    EG: player completed an event with following PlayerEventDirectory,
    {'title': 'rat_fear': 'value': 2}. The players PlayerEventDirectory
    for rat_fear is set to + 2.
    """
    title = models.ForeignKey(PlayerEventTitle)
    value = models.ForeignKey(PlayerEventValue)

    def __str__(self):
        return '{} {}'.format(self.title.title, self.value.value)


class Event(CommonFields):
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField()

    # player event needed for this event
    player_event_needed = models.ManyToManyField(
        PlayerEventDirectory, blank=True,
        related_name='player_event_needed',
    )

    # awards
    player_event_awarded = models.ManyToManyField(
        PlayerEventDirectory, blank=True
    )
    head_armour_awarded = models.ManyToManyField(
        HeadArmour, blank=True
    )
    body_armour_awarded = models.ManyToManyField(
        BodyArmour, blank=True
    )
    backpack_awarded = models.ManyToManyField(
        BackPack, blank=True
    )
    arm_armour_awarded = models.ManyToManyField(
        ArmArmour, blank=True
    )
    leg_armour_awarded = models.ManyToManyField(
        LegArmour, blank=True
    )
    battle_item_awarded = models.ManyToManyField(
        BattleItem, blank=True
    )
    shield_item_awarded = models.ManyToManyField(
        ShieldItem, blank=True
    )

    # player event directory value if completed
    player_event_directory = models.ManyToManyField(
        PlayerEventDirectory, blank=True,
        related_name='player_event_directory',
    )

    # TODO -
    # misc
    # last_event =

    def __str__(self):
        return self.title