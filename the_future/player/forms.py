from django.forms import ModelForm

from account.models import Account
from armour.models import (
    ArmArmour,
    BackPack,
    BodyArmour,
    HeadArmour,
    LegArmour,
)
from player.models import Faction, Player
from item.models import BattleItem, ShieldItem
from utils.custom_form_fields import RelationshipUrlField


class PlayerForm(ModelForm):
    account_url = RelationshipUrlField(
        model_type=Account,
        required=True
    )
    equipped_head_armour_url = RelationshipUrlField(
        model_type=HeadArmour,
        required=False
    )
    equipped_left_arm_armour_url = RelationshipUrlField(
        model_type=ArmArmour,
        required=False
    )
    equipped_left_leg_armour_url = RelationshipUrlField(
        model_type=LegArmour,
        required=False
    )
    equipped_right_arm_armour_url = RelationshipUrlField(
        model_type=ArmArmour,
        required=False
    )
    equipped_right_leg_armour_url = RelationshipUrlField(
        model_type=LegArmour,
        required=False
    )
    equipped_body_armour_url = RelationshipUrlField(
        model_type=BodyArmour,
        required=False
    )
    equipped_backpack_url = RelationshipUrlField(
        model_type=BackPack,
        required=False
    )
    faction_url = RelationshipUrlField(
        model_type=Faction,
        required=False
    )
    equipped_battle_item_url = RelationshipUrlField(
        model_type=BattleItem,
        required=False
    )
    equipped_shield_item_url = RelationshipUrlField(
        model_type=ShieldItem,
        required=False
    )

    def save(self, commit=True, user=None):
        if self.cleaned_data['faction_url'] is not None:
            self.instance.faction = self.cleaned_data['faction_url']
        if self.cleaned_data['account_url'] is not None:
            self.instance.account = self.cleaned_data['account_url']

        # armour
        if self.cleaned_data['equipped_head_armour_url'] is not None:
            self.instance.equipped_head_armour = self.cleaned_data[
                'equipped_head_armour_url']
        if self.cleaned_data['equipped_left_arm_armour_url'] is not None:
            self.instance.equipped_left_arm_armour = self.cleaned_data[
                'equipped_left_arm_armour_url']
        if self.cleaned_data['equipped_left_leg_armour_url'] is not None:
            self.instance.equipped_left_leg_armour = self.cleaned_data[
                'equipped_left_leg_armour_url']
        if self.cleaned_data['equipped_right_arm_armour_url'] is not None:
            self.instance.equipped_right_arm_armour = self.cleaned_data[
                'equipped_right_arm_armour_url']
        if self.cleaned_data['equipped_right_leg_armour_url'] is not None:
            self.instance.equipped_right_leg_armour = self.cleaned_data[
                'equipped_right_leg_armour_url']
        if self.cleaned_data['equipped_body_armour_url'] is not None:
            self.instance.equipped_body_armour = self.cleaned_data[
                'equipped_body_armour_url']
        if self.cleaned_data['equipped_backpack_url'] is not None:
            self.instance.equipped_backpack = self.cleaned_data[
                'equipped_backpack_url']

        # items
        if self.cleaned_data['equipped_battle_item_url'] is not None:
            self.instance.equipped_battle_item = self.cleaned_data[
                'equipped_battle_item_url']
        if self.cleaned_data['equipped_shield_item_url'] is not None:
            self.instance.equipped_shield_item_url = self.cleaned_data[
                'equipped_shield_item_url']

        if user:
            account = Account.objects.get(user=user)

            if not self.instance.created_by:
                self.instance.created_by = account

            self.instance.modified_by = account

        return super(PlayerForm, self).save(commit)

    class Meta:
        model = Player
        exclude = (
            'account',
            'equipped_head_armour',
            'equipped_left_arm_armour',
            'equipped_left_leg_armour',
            'equipped_right_arm_armour',
            'equipped_right_leg_armour',
            'equipped_body_armour',
            'equipped_backpack',
            'faction',
            'created',
            'modified',
            'created_by',
            'modified_by',
            'equipped_battle_item',
            'equipped_shield_item',
        )