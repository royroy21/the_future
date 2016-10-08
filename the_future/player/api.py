from restless.preparers import FieldsPreparer

from utils.generic_resources import (
    COMMON_PREPARE_FIELDS, GenericCrudResource, GenericReadOnlyResource
)
from .forms import PlayerForm
from .models import Faction, Player


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
}
PLAYER_FIELDS.update(COMMON_PREPARE_FIELDS)


class PlayerResource(GenericCrudResource):
    model_cls = Player
    form_cls = PlayerForm

    preparer = FieldsPreparer(fields=PLAYER_FIELDS)

    def prepare(self, data):
        extra_fields = super().prepare(data)
        for field in [
            'equipped_head_armour',
            'equipped_body_armour',
            'equipped_backpack',
            'equipped_left_arm_armour',
            'equipped_left_leg_armour',
            'equipped_right_arm_armour',
            'equipped_right_leg_armour',
            'equipped_battle_item',
            'equipped_shield_item',
        ]:
            field_obj = getattr(data, field)
            field_name = '{}_url'.format(field)
            if field_obj:
                extra_fields[field_name] = field_obj.detail_url
            else:
                extra_fields[field_name] = None

        return extra_fields


class FactionResource(GenericReadOnlyResource):
    model_cls = Faction

    preparer = FieldsPreparer(fields={
        'name': 'name',
        'description': 'description',
    }.update(COMMON_PREPARE_FIELDS))