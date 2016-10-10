from django.db import models

from account.models import Account
from armour.models import (
    ArmArmour, BackPack, BodyArmour, HeadArmour, LegArmour
)
from event.models import PlayerEventDirectory
from item.models import BattleItem, ShieldItem
from utils.generic_models import CommonFields


class Faction(CommonFields):
    name = models.CharField(max_length=255, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class Player(CommonFields):
    account = models.ForeignKey(Account)
    title = models.CharField(max_length=255, blank=True, null=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    faction = models.ForeignKey(Faction, blank=True, null=True)

    # attributes
    melee = models.DecimalField(max_digits=1, decimal_places=0)
    ballistic = models.DecimalField(max_digits=1, decimal_places=0)
    strength = models.DecimalField(max_digits=1, decimal_places=0)
    toughness = models.DecimalField(max_digits=1, decimal_places=0)
    wounds = models.DecimalField(max_digits=1, decimal_places=0)
    initiative = models.DecimalField(max_digits=1, decimal_places=0)
    attacks = models.DecimalField(max_digits=1, decimal_places=0)
    leadership = models.DecimalField(max_digits=1, decimal_places=0)
    health = models.DecimalField(max_digits=1, decimal_places=0)

    # equipped armour
    equipped_head_armour = models.ForeignKey(
        HeadArmour, blank=True, null=True
    )
    equipped_body_armour = models.ForeignKey(
        BodyArmour, blank=True, null=True
    )
    equipped_backpack = models.ForeignKey(
        BackPack, blank=True, null=True
    )
    equipped_left_arm_armour = models.ForeignKey(
        ArmArmour, related_name='left_arm', blank=True, null=True
    )
    equipped_left_leg_armour = models.ForeignKey(
        LegArmour, related_name='left_leg', blank=True, null=True
    )
    equipped_right_arm_armour = models.ForeignKey(
        ArmArmour, related_name='right_arm', blank=True, null=True
    )
    equipped_right_leg_armour = models.ForeignKey(
        LegArmour, related_name='right_leg', blank=True, null=True
    )

    # equipped items
    equipped_battle_item = models.ForeignKey(BattleItem, blank=True, null=True)
    equipped_shield_item = models.ForeignKey(ShieldItem, blank=True, null=True)

    player_event_directory = models.ManyToManyField(
        PlayerEventDirectory, blank=True
    )

    def __str__(self):
        return '({}) {} {} {}'.format(
            self.faction.name, self.title, self.first_name, self.last_name)

