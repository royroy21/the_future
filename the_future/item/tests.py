from django.test import TestCase

from utils.generic_tests import GenericDetailListTests
from .factories import BattleItemFactory, StandardItemFactory


class SharedCreateObjVariables(object):

    def create_obj_variables(self):
        return {
            'created_by': self.account,
            'modified_by': self.account,
        }


class BattleItemTests(SharedCreateObjVariables, GenericDetailListTests,
                      TestCase):
    factory_cls = BattleItemFactory
    url = '/api/battle-item/'


class StandardItemTests(SharedCreateObjVariables, GenericDetailListTests,
                        TestCase):
    factory_cls = StandardItemFactory
    url = '/api/standard-item/'