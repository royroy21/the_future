from django.conf.urls import url
from django.db.models import Q
from restless.preparers import FieldsPreparer

from combat_simulator.forms import CombatRequestForm
from combat_simulator.models import CombatRequest
from utils.generic_resources import (
    COMMON_PREPARE_FIELDS,
    GenericCrudResource,
)


COMBAT_REQUEST_FIELDS = {
    'points': 'points',
    'combat_ready': 'combat_ready',
}
COMBAT_REQUEST_FIELDS.update(COMMON_PREPARE_FIELDS)


class CombatRequestResource(GenericCrudResource):
    model_cls = CombatRequest
    form_cls = CombatRequestForm

    preparer = FieldsPreparer(fields=COMBAT_REQUEST_FIELDS)

    def __init__(self, *args, **kwargs):
        super(CombatRequestResource, self).__init__(*args, **kwargs)

        self.http_methods.update({
            'available': {
                'GET': 'available',
            }
        })

    def available(self):
        """
        Returns all combat requests created or awaiting user players

        This endpoint accepts a player_id parameter so to only show
        results for one user's player
        """
        user_players = self.request.user.account.player_set.filter(
            is_active=True)

        player_id = self.request.GET.get('player_id')
        if player_id:
            user_players.filter(id=player_id)

        return self.model_cls.objects.filter(
            Q(waiting_for_player__in=user_players) |
            Q(initiating_player__in=user_players),
            is_active=True)

    def prepare(self, data):
        extra_fields = super().prepare(data)

        for field in [
            'initiating_player',
            'waiting_for_player',
        ]:
            field_obj = getattr(data, field)
            field_name = '{}_url'.format(field)
            if field_obj:
                extra_fields[field_name] = field_obj.detail_url
            else:
                extra_fields[field_name] = None

        return extra_fields

    @classmethod
    def urls(cls, name_prefix=None):
        urlpatterns = super(CombatRequestResource, cls).urls(
            name_prefix=name_prefix)

        return urlpatterns + [
            url(r'^available/$', cls.as_list('available'),
                name=cls.build_url_name('available', name_prefix)),
        ]