import factory
import random

from item.factories import (
    ArmourFactory,
    ShieldFactory,
    WeaponFactory,
)
from player.factories import FactionFactory, PlayerFactory
from utils.factory_functions import CommonFields

from .models import Hero


class HeroFactory(CommonFields):
    title = random.choice(['Sir', 'Master', 'The Amazing!'])
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    faction = factory.SubFactory(FactionFactory)
    player = factory.SubFactory(PlayerFactory)

    # attributes
    movement = random.choice(range(10))
    melee = random.choice(range(10))
    ballistic = random.choice(range(10))
    strength = random.choice(range(10))
    toughness = random.choice(range(10))
    wounds = random.choice(range(10))
    initiative = random.choice(range(10))
    attacks = random.choice(range(10))
    moral = random.choice(range(10))

    # armour, abilities, items, shield and weapons
    armour = factory.SubFactory(ArmourFactory)
    shield = factory.SubFactory(ShieldFactory)
    weapon_1 = factory.SubFactory(WeaponFactory)
    weapon_2 = factory.SubFactory(WeaponFactory)

    # many to many relations
    @factory.post_generation
    def abilities(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for ability in extracted:
                self.abilities.add(ability)

    @factory.post_generation
    def items(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for item in extracted:
                self.items.add(item)

    class Meta:
        model = Hero