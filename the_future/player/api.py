from copy import copy

from restless.preparers import FieldsPreparer

from utils.generic_resources import (
    COMMON_PREPARE_FIELDS, GenericCrudResource, GenericReadOnlyResource
)
from .forms import PlayerForm
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

PLAYER_FIELDS = {
    'account_url': 'account.detail_url',
    'title': 'title',
    'first_name': 'first_name',
    'last_name': 'last_name',
    'faction_url': 'faction.detail_url',
    'melee': 'melee',
    'ballistic': 'ballistic',
    'strength': 'strength',
    'toughness': 'toughness',
    'wounds': 'wounds',
    'initiative': 'initiative',
    'attacks': 'attacks',
    'leadership': 'leadership',
    'health': 'health',
    # 'head_url': 'head.detail_url',
    # 'left_arm_url': 'left_arm.detail_url',
    # 'left_leg_url': 'left_leg.detail_url',
    # 'right_arm_url': 'right_arm.detail_url',
    # 'right_leg_url': 'right_leg.detail_url',
    # 'body_url': 'body.detail_url',
    # 'backpack_url': 'backpack.detail_url',
}
PLAYER_FIELDS.update(COMMON_PREPARE_FIELDS)


class PlayerResource(GenericCrudResource):
    model_cls = Player
    form_cls = PlayerForm

    preparer = FieldsPreparer(fields=PLAYER_FIELDS)


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