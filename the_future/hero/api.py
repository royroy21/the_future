from restless.preparers import FieldsPreparer

from utils.generic_resources import (
    COMMON_PREPARE_FIELDS, GenericCrudResource
)
from .forms import HeroForm
from .models import Hero


HERO_FIELDS = {
    'player_url': 'player.detail_url',
    'title': 'title',
    'first_name': 'first_name',
    'last_name': 'last_name',
    'faction_url': 'faction.detail_url',
    'movement': 'movement',
    'melee': 'melee',
    'ballistic': 'ballistic',
    'strength': 'strength',
    'toughness': 'toughness',
    'wounds': 'wounds',
    'initiative': 'initiative',
    'attacks': 'attacks',
    'moral': 'moral',
}
HERO_FIELDS.update(COMMON_PREPARE_FIELDS)


class HeroResource(GenericCrudResource):
    model_cls = Hero
    form_cls = HeroForm

    preparer = FieldsPreparer(fields=HERO_FIELDS)

    def prepare(self, data):
        extra_fields = super().prepare(data)
        for field in [
            'armour',
            'shield',
            'weapon_1',
            'weapon_2',
        ]:
            field_obj = getattr(data, field)
            field_name = '{}_url'.format(field)
            if field_obj:
                extra_fields[field_name] = field_obj.detail_url
            else:
                extra_fields[field_name] = None

        for m2m_field in ['abilities', 'items']:
            extra_fields['{}_urls'.format(m2m_field)] = [
                d.detail_url for
                d in getattr(data, m2m_field).filter(is_active=True)]

        return extra_fields