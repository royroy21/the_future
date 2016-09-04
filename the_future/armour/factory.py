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

    # TODO -
    # item = ManyToManyField

    amount_of_items = random.choice(range(10))
    health = random.choice(range(10))
    value = random.choice(range(100))


class ArmArmourFactory(CommonFields, CommonArmourFields):
    class Meta:
        model = ArmArmour


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