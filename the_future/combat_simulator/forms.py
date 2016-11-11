from django.forms import ModelForm

from account.models import Account
from combat_simulator.models import CombatRequest
from hero.models import Hero
from player.models import Player
from utils.custom_form_fields import RelationshipUrlField


class CombatRequestForm(ModelForm):
    initiating_player_url = RelationshipUrlField(
        model_type=Player, required=True,
    )
    initiating_hero_url = RelationshipUrlField(
        model_type=Hero, required=True,
    )
    waiting_for_player_url = RelationshipUrlField(
        model_type=Player, required=True,
    )
    waiting_for_hero_url = RelationshipUrlField(
        model_type=Hero, required=False,
    )

    def save(self, commit=True, user=None):
        if self.cleaned_data['initiating_player_url'] is not None:
            self.instance.initiating_player = self.cleaned_data[
                'initiating_player_url']
        if self.cleaned_data['initiating_hero_url'] is not None:
            self.instance.initiating_hero = self.cleaned_data[
                'initiating_hero_url']
        if self.cleaned_data['waiting_for_player_url'] is not None:
            self.instance.waiting_for_player = self.cleaned_data[
                'waiting_for_player_url']
        if self.cleaned_data['waiting_for_hero_url'] is not None:
            self.instance.waiting_for_hero = self.cleaned_data[
                'waiting_for_hero_url']

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
            'initiating_hero',
            'waiting_for_player_url',
            'waiting_for_hero_url',
            'created',
            'modified',
            'created_by',
            'modified_by',
            'is_active',
        )