import factory
import random

from player.factories import PlayerFactory
from utils.factory_functions import CommonFields

from .models import CombatRequest


class CombatRequestFactory(CommonFields):
    initiating_player = factory.SubFactory(PlayerFactory)

    waiting_for_player = factory.SubFactory(PlayerFactory)

    points = random.randint(0, 999)
    combat_ready = random.choice([True, False])

    class Meta:
        model = CombatRequest