import factory
import random

from utils.factory_functions import CommonFields

from .models import (
    Armour,
    Ability,
    Item,
    Shield,
    Weapon,
)


def random_modifiers(self_attributes=None, enemy_attributes=None):
    """
    :param self_attributes: attributes to take affect on self hero
    :param enemy_attributes: attributes to take affect on enemy hero
    :return:
    {'self': {'strenght': 2}, 'enemy': {'toughness': -1}, 'turns': 1}
    """
    if not self_attributes:
        self_attributes = []

    if not enemy_attributes:
        enemy_attributes = []

    random_modifier = {
        'stages': random.randint(0, 2),
        'self': {}, 'enemy': {},
    }

    for attribute in self_attributes:
        random_modifier['self'][attribute] = random.randint(0, 2)

    for attribute in enemy_attributes:
        random_modifier['enemy'][attribute] = random.randint(-2, 0)

    return random_modifier


class ArmourFactory(CommonFields):
    name = factory.Faker('last_name')
    description = factory.Faker('text')
    modifiers = random_modifiers(self_attributes=['toughness'])
    monetary_value = random.randint(0, 9999999)

    class Meta:
        model = Armour


class AbilityFactory(CommonFields):
    name = factory.Faker('last_name')
    description = factory.Faker('text')
    modifiers = random_modifiers(
        self_attributes=['strength'], enemy_attributes=['toughness'])
    monetary_value = random.randint(0, 9999999)

    class Meta:
        model = Ability


class ItemFactory(CommonFields):
    name = factory.Faker('last_name')
    description = factory.Faker('text')
    modifiers = random_modifiers(
        self_attributes=['strength'], enemy_attributes=['toughness'])
    monetary_value = random.randint(0, 9999999)

    class Meta:
        model = Item


class ShieldFactory(CommonFields):
    name = factory.Faker('last_name')
    description = factory.Faker('text')
    modifiers = random_modifiers(self_attributes=['toughness'])
    monetary_value = random.randint(0, 9999999)

    class Meta:
        model = Shield


class WeaponFactory(CommonFields):
    name = factory.Faker('last_name')
    description = factory.Faker('text')
    modifiers = random_modifiers(self_attributes=['attacks', 'strength'])
    monetary_value = random.randint(0, 9999999)

    class Meta:
        model = Weapon