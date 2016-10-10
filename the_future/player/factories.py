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
from event.factories import PlayerEventDirectoryFactory
from item.factories import BattleItemFactory, ShieldItemFactory
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
    equipped_head_armour = factory.SubFactory(HeadArmourFactory)
    equipped_body_armour = factory.SubFactory(BodyArmourFactory)
    equipped_backpack = factory.SubFactory(BackPackFactory)
    equipped_left_arm_armour = factory.SubFactory(ArmArmourFactory)
    equipped_left_leg_armour = factory.SubFactory(LegArmourFactory)
    equipped_right_arm_armour = factory.SubFactory(ArmArmourFactory)
    equipped_right_leg_armour = factory.SubFactory(LegArmourFactory)
    equipped_battle_item = factory.SubFactory(BattleItemFactory)
    equipped_shield_item = factory.SubFactory(ShieldItemFactory)

    @factory.post_generation
    def player_event_directory(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for group in extracted:
                self.player_event_directory.add(group)

    class Meta:
        model = Player