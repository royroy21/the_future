import factory
import random

from utils.factory_functions import CommonFields

from .models import (
    ArmArmour,
    BackPack,
    BodyArmour,
    HeadArmour,
    LegArmour,
)


class CommonArmourFields(factory.django.DjangoModelFactory):
    name = factory.Faker('name')
    description = factory.Faker('text')
    amount_of_items = random.choice(range(10))
    health = random.choice(range(10))
    value = random.choice(range(100))

    @factory.post_generation
    def items(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of items were passed in, use them
            for item in extracted:
                self.items.add(item)


class ArmArmourFactory(CommonFields, CommonArmourFields):
    class Meta:
        model = ArmArmour

    @factory.post_generation
    def battle_items(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of items were passed in, use them
            for battle_item in extracted:
                self.battle_items.add(battle_item)

class BackPackFactory(CommonFields, CommonArmourFields):
    class Meta:
        model = BackPack


class BodyArmourFactory(CommonFields, CommonArmourFields):
    class Meta:
        model = BodyArmour


class HeadArmourFactory(CommonFields, CommonArmourFields):
    class Meta:
        model = HeadArmour


class LegArmourFactory(CommonFields, CommonArmourFields):
    class Meta:
        model = LegArmour