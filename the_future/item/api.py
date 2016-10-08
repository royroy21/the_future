from restless.preparers import FieldsPreparer

from utils.generic_resources import (
    COMMON_PREPARE_FIELDS, GenericReadOnlyResource
)
from .models import BattleItem, ShieldItem, StandardItem


class BattleItemResource(GenericReadOnlyResource):
    model_cls = BattleItem
    preparer = FieldsPreparer(fields=COMMON_PREPARE_FIELDS)


class ShieldItemResource(GenericReadOnlyResource):
    model_cls = ShieldItem
    preparer = FieldsPreparer(fields=COMMON_PREPARE_FIELDS)


class StandardItemResource(GenericReadOnlyResource):
    model_cls = StandardItem
    preparer = FieldsPreparer(fields=COMMON_PREPARE_FIELDS)