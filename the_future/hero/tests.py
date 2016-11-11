import json

from django.test import TestCase

from hero.factories import HeroFactory
from hero.models import Hero
from item.factories import (
    ArmourFactory,
    AbilityFactory,
    ItemFactory,
    ShieldFactory,
    WeaponFactory,
)
from player.factories import FactionFactory, PlayerFactory
from utils.generic_tests import GenericDetailListTests


class HeroTests(GenericDetailListTests, TestCase):
    factory_cls = HeroFactory
    url = '/api/hero/'

    def create_obj_variables(self):
        faction = FactionFactory()
        player = PlayerFactory()

        armour = ArmourFactory()
        ability = AbilityFactory()
        item = ItemFactory()
        shield = ShieldFactory()
        weapon_1 = WeaponFactory()
        weapon_2 = WeaponFactory()

        return {
            'player': player,
            'title': 'Sir',
            'first_name': 'Roy',
            'last_name': 'Hanley',
            'faction': faction,
            'movement': 4,
            'melee': 4,
            'ballistic': 4,
            'strength': 4,
            'toughness': 4,
            'wounds': 1,
            'initiative': 8,
            'attacks': 1,
            'moral': 7,
            'armour': armour,
            'abilities': [ability],
            'items': [item],
            'shield': shield,
            'weapon_1': weapon_1,
            'weapon_2': weapon_2,
        }

    def test_create_hero(self):
        convert_fields = [
            'player', 'faction',
            'armour', 'abilities',
            'items', 'shield',
            'weapon_1', 'weapon_2',
        ]
        data = self.convert_fields_to_detail_url(
            self.create_obj_variables(), convert_fields
        )

        resp = self.client.post(
            self.url,
            data=json.dumps(data),
            content_type='application/json',
            HTTP_AUTHORIZATION='Bearer {}'.format(self.token)
        )

        r_data = json.loads(resp.content.decode('utf8'))
        self.assertEqual(resp.status_code, 201)

        for k, v in data.items():
            val = v
            if not k.endswith('_urls'):
                val = str(v)
            self.assertEqual(r_data[k], val)

    def test_update_hero(self):
        hero = HeroFactory()
        armour_2 = ArmourFactory()

        get_resp = self.client.get(
            hero.detail_url,
            HTTP_AUTHORIZATION='Bearer {}'.format(self.token),
        )
        get_data = json.loads(get_resp.content.decode('utf8'))

        first_name = 'Cat'
        last_name = 'Meow'
        get_data['first_name'] = first_name
        get_data['last_name'] = last_name
        get_data['armour_url'] = armour_2.detail_url

        put_resp = self.client.put(
            hero.detail_url,
            data=json.dumps(get_data),
            content_type='application/json',
            HTTP_AUTHORIZATION='Bearer {}'.format(self.token),
        )
        put_data = json.loads(put_resp.content.decode('utf8'))

        self.assertEqual(put_resp.status_code, 202)
        self.assertEqual(put_data['first_name'], first_name)
        self.assertEqual(put_data['last_name'], last_name)
        self.assertEqual(
            put_data['armour_url'], armour_2.detail_url
        )

    def test_delete_hero(self):
        hero = HeroFactory()
        self.assertTrue(
            Hero.objects.filter(id=hero.id, is_active=True).exists()
        )

        resp = self.client.delete(
            hero.detail_url,
            HTTP_AUTHORIZATION='Bearer {}'.format(self.token),
        )
        self.assertEqual(resp.status_code, 204)
        self.assertFalse(
            Hero.objects.filter(id=hero.id, is_active=True).exists()
        )

    def test_hero_factory(self):
        ability = AbilityFactory()
        item = ItemFactory()
        hero = HeroFactory(abilities=[ability], items=[item])

        self.assertTrue(hero.armour)
        self.assertIn(ability, hero.abilities.all())
        self.assertIn(item, hero.items.all())