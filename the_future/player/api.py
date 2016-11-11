from restless.preparers import FieldsPreparer

from utils.generic_resources import (
    COMMON_PREPARE_FIELDS, GenericCrudResource, GenericReadOnlyResource
)
from player.forms import PlayerForm
from player.models import Faction, Player


PLAYER_FIELDS = {
    'account_url': 'account.detail_url',
    'title': 'title',
    'first_name': 'first_name',
    'last_name': 'last_name',
    'faction_url': 'faction.detail_url',
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