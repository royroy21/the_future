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
from utils.custom_form_fields import RelationshipUrlField


class PlayerForm(ModelForm):
    account_url = RelationshipUrlField(
        model_type=Account,
        required=True
    )
    head_url = RelationshipUrlField(
        model_type=HeadArmour,
        required=False
    )
    left_arm_url = RelationshipUrlField(
        model_type=ArmArmour,
        required=False
    )
    left_leg_url = RelationshipUrlField(
        model_type=LegArmour,
        required=False
    )
    right_arm_url = RelationshipUrlField(
        model_type=ArmArmour,
        required=False
    )
    right_leg_url = RelationshipUrlField(
        model_type=LegArmour,
        required=False
    )
    body_url = RelationshipUrlField(
        model_type=BodyArmour,
        required=False
    )
    backpack_url = RelationshipUrlField(
        model_type=BackPack,
        required=False
    )
    faction_url = RelationshipUrlField(
        model_type=Faction,
        required=False
    )

    def save(self, commit=True, user=None):
        if self.cleaned_data['account_url'] is not None:
            self.instance.account = self.cleaned_data['account_url']
        if self.cleaned_data['head_url'] is not None:
            self.instance.head = self.cleaned_data['head_url']
        if self.cleaned_data['left_arm_url'] is not None:
            self.instance.left_arm = self.cleaned_data['left_arm_url']
        if self.cleaned_data['left_leg_url'] is not None:
            self.instance.left_leg = self.cleaned_data['left_leg_url']
        if self.cleaned_data['right_arm_url'] is not None:
            self.instance.right_arm = self.cleaned_data['right_arm_url']
        if self.cleaned_data['right_leg_url'] is not None:
            self.instance.right_leg = self.cleaned_data['right_leg_url']
        if self.cleaned_data['body_url'] is not None:
            self.instance.body = self.cleaned_data['body_url']
        if self.cleaned_data['backpack_url'] is not None:
            self.instance.backpack = self.cleaned_data['backpack_url']
        if self.cleaned_data['faction_url'] is not None:
            self.instance.faction = self.cleaned_data['faction_url']

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
            'head',
            'left_arm',
            'left_leg',
            'right_arm',
            'right_leg',
            'body',
            'backpack',
            'faction',
            'created',
            'modified',
            'created_by',
            'modified_by',
        )