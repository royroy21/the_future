from restless.preparers import FieldsPreparer

from utils.generic_resources import (
    COMMON_PREPARE_FIELDS, GenericReadOnlyResource
)
from .models import (
    Armour,
    Ability,
    Item,
    Shield,
    Weapon,
)


ARMOUR_COMMON_FIELDS = {
    'name': 'name',
    'description': 'description',
    'modifiers': 'modifiers',
    'monetary_value': 'monetary_value',
}
ARMOUR_COMMON_FIELDS.update(COMMON_PREPARE_FIELDS)


class ArmourResource(GenericReadOnlyResource):
    model_cls = Armour
    preparer = FieldsPreparer(fields=ARMOUR_COMMON_FIELDS)


class AbilityResource(GenericReadOnlyResource):
    model_cls = Ability
    preparer = FieldsPreparer(fields=ARMOUR_COMMON_FIELDS)


class ItemResource(GenericReadOnlyResource):
    model_cls = Item
    preparer = FieldsPreparer(fields=ARMOUR_COMMON_FIELDS)


class ShieldResource(GenericReadOnlyResource):
    model_cls = Shield
    preparer = FieldsPreparer(fields=ARMOUR_COMMON_FIELDS)


class WeaponResource(GenericReadOnlyResource):
    model_cls = Weapon
    preparer = FieldsPreparer(fields=ARMOUR_COMMON_FIELDS)