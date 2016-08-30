from django.test import TestCase

from utils.generic_tests import GenericDetailListTests
from .models import BattleItem, StandardItem


class SharedCreateObjVariables(object):

    def create_obj_variables(self):
        return {
            'created_by': self.account,
            'modified_by': self.account,
        }


class BattleItemTests(SharedCreateObjVariables, GenericDetailListTests,
                      TestCase):
    model_cls = BattleItem
    url = '/api/battle-item/'


class StandardItemTests(SharedCreateObjVariables, GenericDetailListTests,
                        TestCase):
    model_cls = StandardItem
    url = '/api/standard-item/'