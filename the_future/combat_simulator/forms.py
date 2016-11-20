from django.forms import ModelForm
from restless.exceptions import BadRequest

from account.models import Account
from combat_simulator.models import CombatRequest
from player.models import Player
from utils.custom_form_fields import RelationshipUrlField


class CombatRequestForm(ModelForm):
    initiating_player_url = RelationshipUrlField(
        model_type=Player, required=True,
    )
    waiting_for_player_url = RelationshipUrlField(
        model_type=Player, required=True,
    )

    def save(self, commit=True, user=None):
        if self.cleaned_data['initiating_player_url'] is not None:
            self.instance.initiating_player = self.cleaned_data[
                'initiating_player_url']
        if self.cleaned_data['waiting_for_player_url'] is not None:
            self.instance.waiting_for_player = self.cleaned_data[
                'waiting_for_player_url']

        # only "waiting for player" player may set a combat request
        # to ready. If "waiting for player" does not set combat-ready
        # to True the whole combat request is cancelled
        user_players = user.account.player_set.filter(is_active=True)
        if self.cleaned_data['waiting_for_player_url'] in user_players:
            if not self.cleaned_data['combat_ready']:
                self.instance.is_active = False
        else:
            if self.cleaned_data['combat_ready']:
                raise BadRequest('only "waiting for player" can ready combat')

        if user:
            account = Account.objects.get(user=user)
            if not self.instance.created_by:
                self.instance.created_by = account
            self.instance.modified_by = account

        return super(CombatRequestForm, self).save(commit)

    class Meta:
        model = CombatRequest
        exclude = (
            'initiating_player',
            'waiting_for_player_url',
            'created',
            'modified',
            'created_by',
            'modified_by',
            'is_active',
        )