import factory
import random

from account.factories import AccountFactory
from armour.factories import (
    ArmArmourFactory,
    BackPackFactory,
    BodyArmourFactory,
    HeadArmourFactory,
    LegArmourFactory,
)
from utils.factory_functions import CommonFields

from .models import Faction, Player


class FactionFactory(CommonFields):
    name = random.choice(['Vampires', 'Werewolves'])
    description = factory.Faker('text')

    class Meta:
        model = Faction


class PlayerFactory(CommonFields):
    account = factory.SubFactory(AccountFactory)
    title = random.choice(['Sir', 'Master', 'The Amazing!'])
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    faction = factory.SubFactory(FactionFactory)
    melee = random.choice(range(10))
    ballistic = random.choice(range(10))
    strength = random.choice(range(10))
    toughness = random.choice(range(10))
    wounds = random.choice(range(10))
    initiative = random.choice(range(10))
    attacks = random.choice(range(10))
    leadership = random.choice(range(10))
    health = random.choice(range(10))
    head = factory.SubFactory(HeadArmourFactory)
    body = factory.SubFactory(BodyArmourFactory)
    backpack = factory.SubFactory(BackPackFactory)
    left_arm = factory.SubFactory(ArmArmourFactory)
    left_leg = factory.SubFactory(LegArmourFactory)
    right_arm = factory.SubFactory(ArmArmourFactory)
    right_leg = factory.SubFactory(LegArmourFactory)

    class Meta:
        model = Player