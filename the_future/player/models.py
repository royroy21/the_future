from django.db import models

from account.models import Account
from utils.generic_models import CommonFields


class Player(CommonFields):
    account = models.ForeignKey(Account)
    title = models.CharField(max_length=255, blank=True, null=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    faction = models.ForeignKey('Faction', blank=True, null=True)

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

    # armour
    head = models.ForeignKey('Head', blank=True, null=True)
    body = models.ForeignKey('BodyArmour', blank=True, null=True)
    backpack = models.ForeignKey('Backpack', blank=True, null=True)
    left_arm = models.ForeignKey('ArmArmour', related_name='left_arm',
                                 blank=True, null=True)
    left_leg = models.ForeignKey('LegArmour', related_name='left_leg',
                                 blank=True, null=True)
    right_arm = models.ForeignKey('ArmArmour', related_name='right_arm',
                                  blank=True, null=True)
    right_leg = models.ForeignKey('LegArmour', related_name='right_leg',
                                  blank=True, null=True)

    def __str__(self):
        return '({}) {} {} {}'.format(
            self.faction.name, self.title, self.first_name, self.last_name)


class Faction(CommonFields):
    name = models.CharField(max_length=255, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class Armour(CommonFields):
    name = models.CharField(max_length=255)
    description = models.TextField()
    item = models.ManyToManyField('Item', blank=True)
    amount_of_items = models.DecimalField(max_digits=2, decimal_places=0)
    health = models.DecimalField(max_digits=2, decimal_places=0)
    value = models.DecimalField(max_digits=7, decimal_places=0)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class ArmArmour(Armour):
    battle_item = models.ForeignKey('BattleItem')

    def __str__(self):
        return self.name


class Head(Armour):
    pass


class LegArmour(Armour):
    pass


class BodyArmour(Armour):
    pass


class BackPack(Armour):
    pass


# Will move to battle items app
class BattleItem(CommonFields):
    pass


# Will move to items app
class Item(CommonFields):
    pass