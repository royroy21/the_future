from django.test import TestCase

from utils.generic_tests import GenericDetailListTests
from item.models import BattleItem
from .models import (
    ArmArmour, BackPack, BodyArmour, HeadArmour, LegArmour
)


class SharedCreateObjVariables(object):

    def create_obj_variables(self):
        return {
            'created_by': self.account,
            'modified_by': self.account,
            'name': 'test name',
            # 'description:': 'test description',
            'amount_of_items': 2,
            'health': 9,
            'value': 100,
        }


class LegArmourTests(SharedCreateObjVariables, GenericDetailListTests,
                     TestCase):
    model_cls = LegArmour
    url = '/api/leg-armour/'


class ArmArmourTests(SharedCreateObjVariables, GenericDetailListTests,
                     TestCase):
    model_cls = ArmArmour
    url = '/api/arm-armour/'

    def create_obj_variables(self):
        obj_vars = super().create_obj_variables()
        obj_vars['battle_item'] = BattleItem.objects.create()
        return obj_vars


class HeadArmourTests(SharedCreateObjVariables, GenericDetailListTests,
                      TestCase):
    model_cls = HeadArmour
    url = '/api/head-armour/'


class BodyArmourTests(SharedCreateObjVariables, GenericDetailListTests,
                      TestCase):
    model_cls = BodyArmour
    url = '/api/body-armour/'


class BackPackTests(SharedCreateObjVariables, GenericDetailListTests,
                    TestCase):
    model_cls = BackPack
    url = '/api/back-pack/'