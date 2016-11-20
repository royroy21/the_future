from django.db import models

from player.models import Player
from utils.generic_models import CommonFields


class CombatRequest(CommonFields):
    """
    When player requests combat with another player an entry
    is created here with a points value for combat.

    All player apps will poll a URL telling them if any combat
    requests are meant for them. If a request is available the
    player will either accept or decline.

    The initiating player polls this entry to see if the other
    player has accepted.

    When both players have accepted a combat simulator URL is sent
    to both players.
    """
    initiating_player = models.ForeignKey(Player)
    points = models.DecimalField(
        max_digits=999, decimal_places=0, null=True, blank=True)

    waiting_for_player = models.ForeignKey(
        Player, blank=True, null=True, related_name='waiting_for_player')

    # set to true when waiting for player accepts combat
    combat_ready = models.BooleanField(default=False)

    def __str__(self):
        replace_key = '(NO ONE)'
        base_str = '{} fights {}'.format(self.initiating_player, replace_key)

        if self.waiting_for_player and self.waiting_for_hero:
            base_str.replace(replace_key, self.waiting_for_hero)

        return base_str