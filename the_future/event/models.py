from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

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
        return str(self.value)


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

    # player event directory value if completed
    player_event_directory = models.ManyToManyField(
        PlayerEventDirectory, blank=True,
        related_name='player_event_directory',
    )

    # event content
    content_type = models.ForeignKey(ContentType, null=True, blank=True)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    def __str__(self):
        return self.title