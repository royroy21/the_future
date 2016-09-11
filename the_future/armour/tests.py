from django.test import TestCase

from utils.generic_tests import GenericDetailListTests
from item.factories import BattleItemFactory, StandardItemFactory
from .factories import (
    ArmArmourFactory, BackPackFactory, BodyArmourFactory,
    HeadArmourFactory, LegArmourFactory
)


class LegArmourTests(GenericDetailListTests, TestCase):
    factory_cls = LegArmourFactory
    url = '/api/leg-armour/'


class ArmArmourTests(GenericDetailListTests, TestCase):
    factory_cls = ArmArmourFactory
    url = '/api/arm-armour/'

    def _create_test_obj(self):
        battle_item = BattleItemFactory()
        item_1 = StandardItemFactory()
        item_2 = StandardItemFactory()
        return self.factory_cls(
            battle_items=(battle_item,),
            items=(item_1, item_2),
        )


class HeadArmourTests(GenericDetailListTests, TestCase):
    factory_cls = HeadArmourFactory
    url = '/api/head-armour/'


class BodyArmourTests(GenericDetailListTests, TestCase):
    factory_cls = BodyArmourFactory
    url = '/api/body-armour/'


class BackPackTests(GenericDetailListTests, TestCase):
    factory_cls = BackPackFactory
    url = '/api/back-pack/'