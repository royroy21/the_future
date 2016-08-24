from copy import copy

from restless.preparers import FieldsPreparer

from utils.generic_resources import (
    COMMON_PREPARE_FIELDS, GenericCrudResource, GenericReadOnlyResource
)
from .models import (
    ArmArmour, BackPack, BodyArmour, Faction, Head, Player, LegArmour
)


GENERIC_ARMOUR_FIELDS = {
    'name': 'name',
    'description': 'description',
    # 'item': 'item',
    'amount_of_items': 'amount_of_items',
    'health': 'health',
    'value': 'value',
}
GENERIC_ARMOUR_FIELDS.update(COMMON_PREPARE_FIELDS)
GENERIC_ARMOUR_FIELDS_PlUS_WEAPON = copy(GENERIC_ARMOUR_FIELDS)
GENERIC_ARMOUR_FIELDS_PlUS_WEAPON.update(
    {'battle_item': 'battle_item'})


class PlayerResource(GenericCrudResource):

    model_cls = Player

    preparer = FieldsPreparer(fields={
        'account': 'account.detail_url',
        'title': 'title',
        'first_name': 'first_name',
        'last_name': 'last_name',
        'faction': 'faction',
        'melee': 'melee',
        'ballistic': 'ballistic',
        'strength': 'strength',
        'toughness': 'toughness',
        'wounds': 'wounds',
        'initiative': 'initiative',
        'attacks': 'attacks',
        'leadership': 'leadership',
        'health': 'health',
        'head': 'head',
        'left_arm': 'left_arm',
        'left_leg': 'left_leg',
        'right_arm': 'right_arm',
        'right_leg': 'right_leg',
        'body': 'body',
        'backpack': 'backpack',
    }.update(COMMON_PREPARE_FIELDS))


class FactionResource(GenericReadOnlyResource):
    model_cls = Faction

    preparer = FieldsPreparer(fields={
        'name': 'name',
        'description': 'description',
    }.update(COMMON_PREPARE_FIELDS))


class ArmArmourResource(GenericReadOnlyResource):
    model_cls = ArmArmour
    preparer = FieldsPreparer(fields=GENERIC_ARMOUR_FIELDS_PlUS_WEAPON)


class HeadResource(GenericReadOnlyResource):
    model_cls = Head
    preparer = FieldsPreparer(fields=GENERIC_ARMOUR_FIELDS)


class LegArmourResource(GenericReadOnlyResource):
    model_cls = LegArmour
    preparer = FieldsPreparer(fields=GENERIC_ARMOUR_FIELDS)


class BodyArmourResource(GenericReadOnlyResource):
    model_cls = BodyArmour
    preparer = FieldsPreparer(fields=GENERIC_ARMOUR_FIELDS)


class BackPackResource(GenericReadOnlyResource):
    model_cls = BackPack
    preparer = FieldsPreparer(fields=GENERIC_ARMOUR_FIELDS)