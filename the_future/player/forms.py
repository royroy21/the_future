from django.forms import ModelForm

from account.models import Account
from player.models import (
    ArmArmour,
    BackPack,
    BodyArmour,
    Faction,
    Head,
    LegArmour,
    Player,
)
from utils.custom_form_fields import RelationshipUrlField


class PlayerFrom(ModelForm):
    account_url = RelationshipUrlField(
        model_type=Account,
        required=True
    )
    head_url = RelationshipUrlField(
        model_type=Head,
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

    class Meta:
        model = Player
        exclude = [
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
        ]