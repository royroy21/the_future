from django.db import models

from item.models import (
    Item,
    Weapon,
    Shield,
    Armour,
    Ability,
)
from player.models import Faction, Player
from utils.generic_models import CommonFields


class Hero(CommonFields):
    title = models.CharField(max_length=255, blank=True, null=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    faction = models.ForeignKey(Faction, blank=True, null=True)
    player = models.ForeignKey(Player)

    # attributes
    movement = models.DecimalField(max_digits=1, decimal_places=0)
    melee = models.DecimalField(max_digits=1, decimal_places=0)
    ballistic = models.DecimalField(max_digits=1, decimal_places=0)
    strength = models.DecimalField(max_digits=1, decimal_places=0)
    toughness = models.DecimalField(max_digits=1, decimal_places=0)
    wounds = models.DecimalField(max_digits=1, decimal_places=0)
    initiative = models.DecimalField(max_digits=1, decimal_places=0)
    attacks = models.DecimalField(max_digits=1, decimal_places=0)
    moral = models.DecimalField(max_digits=1, decimal_places=0)

    # armour, shield, abilities, items and weapons
    armour = models.ForeignKey(Armour, blank=True, null=True)
    shield = models.ForeignKey(Shield, blank=True, null=True)
    weapon_1 = models.ForeignKey(
        Weapon, blank=True, null=True, related_name='weapon_1')
    weapon_2 = models.ForeignKey(
        Weapon, blank=True, null=True, related_name='weapon_2')
    abilities = models.ManyToManyField(Ability, blank=True, null=True)
    items = models.ManyToManyField(Item, blank=True, null=True)

    def __str__(self):
        faction_name = self.faction.name if self.faction else None
        return '({}) {} {} {}'.format(
            faction_name, self.title, self.first_name, self.last_name)
