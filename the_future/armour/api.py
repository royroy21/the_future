from restless.preparers import FieldsPreparer

from utils.generic_resources import (
    COMMON_PREPARE_FIELDS, GenericReadOnlyResource
)
from .models import ArmArmour, BackPack, BodyArmour, HeadArmour, LegArmour


GENERIC_ARMOUR_FIELDS = {
    'name': 'name',
    'description': 'description',
    'amount_of_items': 'amount_of_items',
    'health': 'health',
    'value': 'value',
}
GENERIC_ARMOUR_FIELDS.update(COMMON_PREPARE_FIELDS)


class GenericReadOnlyWithPreparedItems(GenericReadOnlyResource):
    def prepare(self, data):
        extra_fields = super().prepare(data)
        extra_fields['item_urls'] = [
            o.detail_url for o in data.items.all()
        ]
        return extra_fields


class ArmArmourResource(GenericReadOnlyWithPreparedItems):
    model_cls = ArmArmour
    preparer = FieldsPreparer(fields=GENERIC_ARMOUR_FIELDS)

    def prepare(self, data):
        extra_fields = super().prepare(data)
        extra_fields['battle_item_urls'] = [
            o.detail_url for o in data.battle_items.all()
        ]
        return extra_fields


class HeadArmourResource(GenericReadOnlyWithPreparedItems):
    model_cls = HeadArmour
    preparer = FieldsPreparer(fields=GENERIC_ARMOUR_FIELDS)


class LegArmourResource(GenericReadOnlyWithPreparedItems):
    model_cls = LegArmour
    preparer = FieldsPreparer(fields=GENERIC_ARMOUR_FIELDS)


class BodyArmourResource(GenericReadOnlyWithPreparedItems):
    model_cls = BodyArmour
    preparer = FieldsPreparer(fields=GENERIC_ARMOUR_FIELDS)


class BackPackResource(GenericReadOnlyWithPreparedItems):
    model_cls = BackPack
    preparer = FieldsPreparer(fields=GENERIC_ARMOUR_FIELDS)