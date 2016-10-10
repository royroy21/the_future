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
    pass

    class Meta:
        model = Event