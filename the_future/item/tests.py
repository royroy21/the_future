from django.test import TestCase

from utils.generic_tests import GenericDetailListTests
from .factories import (
    ArmourFactory,
    AbilityFactory,
    ItemFactory,
    ShieldFactory,
    WeaponFactory,
)


class SharedCreateObjVariables(object):

    def create_obj_variables(self):
        return {
            'created_by': self.account,
            'modified_by': self.account,
        }


class ArmourTests(SharedCreateObjVariables, GenericDetailListTests, TestCase):
    factory_cls = ArmourFactory
    url = '/api/armour/'


class AbilityTests(SharedCreateObjVariables, GenericDetailListTests, TestCase):
    factory_cls = AbilityFactory
    url = '/api/ability/'


class ItemTests(SharedCreateObjVariables, GenericDetailListTests, TestCase):
    factory_cls = ItemFactory
    url = '/api/item/'


class ShieldTests(SharedCreateObjVariables, GenericDetailListTests, TestCase):
    factory_cls = ShieldFactory
    url = '/api/shield/'


class WeaponTests(SharedCreateObjVariables, GenericDetailListTests, TestCase):
    factory_cls = WeaponFactory
    url = '/api/weapon/'