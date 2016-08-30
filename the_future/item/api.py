from restless.preparers import FieldsPreparer

from utils.generic_resources import (
    COMMON_PREPARE_FIELDS, GenericReadOnlyResource
)
from .models import BattleItem, StandardItem


class BattleItemResource(GenericReadOnlyResource):
    model_cls = BattleItem
    preparer = FieldsPreparer(fields=COMMON_PREPARE_FIELDS)


class StandardItemResource(GenericReadOnlyResource):
    model_cls = StandardItem
    preparer = FieldsPreparer(fields=COMMON_PREPARE_FIELDS)