from django.db import models

from hero.models import Hero
from player.models import Player
from utils.generic_models import CommonFields


class CombatRequest(CommonFields):
    """
    When player requests combat with another player an entry
    is created here.

    All player apps will poll a URL telling them if any combat
    requests are meant for them. If a request is available the
    player will either accept or decline with a hero of equal or
    less level than the initiating player.

    The initiating player polls this entry to see if the another
    player has accepted.

    When both players have accepted a combat simulator URL is sent
    to both players.
    """
    initiating_player = models.ForeignKey(Player)
    initiating_hero = models.ForeignKey(Hero)

    waiting_for_player = models.ForeignKey(
        Player, blank=True, null=True, related_name='waiting_for_player')
    waiting_for_hero = models.ForeignKey(
        Hero, blank=True, null=True, related_name='waiting_for_hero')

    def __str__(self):
        replace_key = '(NO ONE)'

        base_str = '{} with {} fights {}'.format(
            self.initiating_player, self.initiating_hero, replace_key)
        if self.waiting_for_player and self.waiting_for_hero:
            base_str.replace(replace_key, '{} with {}'.format(
                self.waiting_for_player, self.waiting_for_hero))

        return base_str