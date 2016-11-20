from django.forms import ModelForm

from account.models import Account
from item.models import (
    Item,
    Weapon,
    Shield,
    Armour,
    Ability,
)
from player.models import Faction, Player
from utils.custom_form_fields import (
    RelationshipMultipleUrlField, RelationshipUrlField,
)

from .models import Hero


class HeroForm(ModelForm):
    player_url = RelationshipUrlField(
        model_type=Player, required=True,
    )
    faction_url = RelationshipUrlField(
        model_type=Faction, required=True,
    )
    weapon_1_url = RelationshipUrlField(
        model_type=Weapon, required=False,
    )
    weapon_2_url = RelationshipUrlField(
        model_type=Weapon, required=False,
    )
    shield_url = RelationshipUrlField(
        model_type=Shield, required=False,
    )
    armour_url = RelationshipUrlField(
        model_type=Armour, required=False,
    )
    items_urls = RelationshipMultipleUrlField(
        model_type=Item, required=False,
    )
    abilities_urls = RelationshipMultipleUrlField(
        model_type=Ability, required=False,
    )

    def save(self, commit=True, user=None):
        if self.cleaned_data['player_url'] is not None:
            self.instance.player = self.cleaned_data['player_url']
        if self.cleaned_data['faction_url'] is not None:
            self.instance.faction = self.cleaned_data['faction_url']
        if self.cleaned_data['weapon_1_url'] is not None:
            self.instance.weapon_1 = self.cleaned_data['weapon_1_url']
        if self.cleaned_data['weapon_2_url'] is not None:
            self.instance.weapon_2 = self.cleaned_data['weapon_2_url']
        if self.cleaned_data['armour_url'] is not None:
            self.instance.armour = self.cleaned_data['armour_url']
        if self.cleaned_data['shield_url'] is not None:
            self.instance.shield = self.cleaned_data['shield_url']

        self.instance.save()
        for m2m_field in ['abilities', 'items']:
            for item in self.cleaned_data['{}_urls'.format(m2m_field)]:
                getattr(self.instance, m2m_field).add(item)

        if user:
            account = Account.objects.get(user=user)
            if not self.instance.created_by:
                self.instance.created_by = account
            self.instance.modified_by = account

        return super(HeroForm, self).save(commit)

    class Meta:
        model = Hero
        exclude = (
            'faction',
            'player',
            'weapon_1',
            'weapon_2',
            'armour',
            'shield',
            'items',
            'abilities',
            'created',
            'modified',
            'created_by',
            'modified_by',
            'is_active',
        )