from restless.exceptions import BadRequest
from restless.preparers import FieldsPreparer

from combat_simulator.forms import CombatRequestForm
from combat_simulator.models import CombatRequest
from player.models import Player
from utils.generic_resources import (
    COMMON_PREPARE_FIELDS,
    GenericCrudResource,
)
from utils.url_to_object import url_to_object


class CombatRequestResource(GenericCrudResource):
    model_cls = CombatRequest
    form_cls = CombatRequestForm

    preparer = FieldsPreparer(fields=COMMON_PREPARE_FIELDS)

    def __init__(self, *args, **kwargs):
        super(CombatRequestResource, self).__init__(*args, **kwargs)

        # TODO!
        self.http_methods.update({
            'schema': {
                'GET': 'schema',
            }
        })

    def request_combat(self, player_url):
        player_obj = url_to_object(player_url)

        if not isinstance(Player, player_obj):
            raise BadRequest('player_url does not resolve to Player')

        return CombatRequest.objects.filter(
            is_active=True, waiting_for_player=player_obj)

    def prepare(self, data):
        extra_fields = super().prepare(data)

        for field in [
            'initiating_player',
            'initiating_hero',
            'waiting_for_player',
            'waiting_for_hero',
        ]:
            field_obj = getattr(data, field)
            field_name = '{}_url'.format(field)
            if field_obj:
                extra_fields[field_name] = field_obj.detail_url
            else:
                extra_fields[field_name] = None

        # combat is ready when all heroes and players are ready
        if all([
            data.initiating_player,
            data.initiating_hero,
            data.waiting_for_player,
            data.waiting_for_hero,
        ]):
            extra_fields['combat_ready'] = True
        else:
            extra_fields['combat_ready'] = False

        return extra_fields