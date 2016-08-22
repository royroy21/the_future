from django.db import models
from django.utils import timezone


class Player(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    faction = models.ForeignKey('Faction')

    # attributes
    coordination = models.DecimalField(max_digits=2, decimal_places=0)
    luck = models.DecimalField(max_digits=2, decimal_places=0)
    awareness = models.DecimalField(max_digits=2, decimal_places=0)
    strength = models.DecimalField(max_digits=2, decimal_places=0)
    speed = models.DecimalField(max_digits=2, decimal_places=0)
    intelligent = models.DecimalField(max_digits=2, decimal_places=0)
    charisma = models.DecimalField(max_digits=2, decimal_places=0)
    health = models.DecimalField(max_digits=2, decimal_places=0)
    lives = models.DecimalField(max_digits=2, decimal_places=0)

    # armour
    head = models.ForeignKey('Head')
    left_arm = models.ForeignKey('ArmArmour', related_name='left_arm')
    left_leg = models.ForeignKey('LegArmour', related_name='left_leg')
    right_arm = models.ForeignKey('ArmArmour', related_name='right_arm')
    right_leg = models.ForeignKey('LegArmour', related_name='right_leg')
    body = models.ForeignKey('BodyArmour')
    backpack = models.ForeignKey('Backpack')

    created = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return '({}) {} {} {}'.format(
            self.faction.name, self.title, self.first_name, self.last_name)


class Faction(models.Model):
    name = models.CharField(max_length=255, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class Armour(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    item = models.ManyToManyField('Item')
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
class BattleItem(models.Model):
    pass


# Will move to items app
class Item(models.Model):
    pass