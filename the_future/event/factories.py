import factory
import random

from utils.factory_functions import CommonFields

from .models import (
    PlayerEventTitle, PlayerEventValue, PlayerEventDirectory, Event
)


class PlayerEventTitleFactory(CommonFields):
    title = random.choice(['rat_fear', 'computers', 'throwing'])

    class Meta:
        model = PlayerEventTitle


class PlayerEventValueFactory(CommonFields):
    value = random.choice([-3, -2, -1, 0, 1, 2, 3])

    class Meta:
        model = PlayerEventValue


class PlayerEventDirectoryFactory(CommonFields):
    title = factory.SubFactory(PlayerEventTitleFactory)
    value = factory.SubFactory(PlayerEventValueFactory)

    class Meta:
        model = PlayerEventDirectory


# TODO
class EventFactory(CommonFields):

    @factory.post_generation
    def player_event_needed(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for group in extracted:
                self.player_event_needed.add(group)

    @factory.post_generation
    def player_event_directory(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for group in extracted:
                self.player_event_directory.add(group)

    class Meta:
        model = Event