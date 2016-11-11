import factory

from hero.factories import HeroFactory
from player.factories import PlayerFactory
from utils.factory_functions import CommonFields

from .models import CombatRequest


class CombatRequestFactory(CommonFields):
    initiating_player = factory.SubFactory(PlayerFactory)
    initiating_hero = factory.SubFactory(HeroFactory)

    waiting_for_player = factory.SubFactory(PlayerFactory)
    waiting_for_hero = factory.SubFactory(HeroFactory)

    class Meta:
        model = CombatRequest