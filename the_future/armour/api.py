from restless.preparers import FieldsPreparer

from utils.generic_resources import (
    COMMON_PREPARE_FIELDS, GenericReadOnlyResource
)
from .models import ArmArmour, BackPack, BodyArmour, HeadArmour, LegArmour


GENERIC_ARMOUR_FIELDS = {
    'name': 'name',
    'description': 'description',
    'health': 'health',
    'value': 'value',
}
GENERIC_ARMOUR_FIELDS.update(COMMON_PREPARE_FIELDS)


class ArmArmourResource(GenericReadOnlyResource):
    model_cls = ArmArmour
    preparer = FieldsPreparer(fields=GENERIC_ARMOUR_FIELDS)


class HeadArmourResource(GenericReadOnlyResource):
    model_cls = HeadArmour
    preparer = FieldsPreparer(fields=GENERIC_ARMOUR_FIELDS)


class LegArmourResource(GenericReadOnlyResource):
    model_cls = LegArmour
    preparer = FieldsPreparer(fields=GENERIC_ARMOUR_FIELDS)


class BodyArmourResource(GenericReadOnlyResource):
    model_cls = BodyArmour
    preparer = FieldsPreparer(fields=GENERIC_ARMOUR_FIELDS)


class BackPackResource(GenericReadOnlyResource):
    model_cls = BackPack
    preparer = FieldsPreparer(fields=GENERIC_ARMOUR_FIELDS)