import json

from django.test import TestCase

from armour.factories import ArmArmourFactory
from event.factories import PlayerEventDirectoryFactory
from player.factories import FactionFactory, PlayerFactory, LegArmourFactory
from player.models import Player
from utils.generic_tests import GenericDetailListTests


class PlayerTests(GenericDetailListTests, TestCase):
    factory_cls = PlayerFactory
    url = '/api/player/'

    white_list_for_test_field = ['player_event_directory_urls']

    def create_obj_variables(self):
        faction = FactionFactory()
        left_leg_armour = LegArmourFactory()
        right_leg_armour = LegArmourFactory()

        return {
            'account': self.account,
            'title': 'Sir',
            'first_name': 'Roy',
            'last_name': 'Hanley',
            'faction': faction,
            'melee': 4,
            'ballistic': 4,
            'strength': 4,
            'toughness': 4,
            'wounds': 1,
            'initiative': 8,
            'attacks': 1,
            'leadership': 7,
            'health': 9,
            'equipped_left_leg_armour': left_leg_armour,
            'equipped_right_leg_armour': right_leg_armour,
        }

    def test_create_player(self):
        convert_fields = [
            'account', 'faction',
            'equipped_left_leg_armour',
            'equipped_right_leg_armour'
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
            self.assertEqual(r_data[k], str(v))

    def test_update_player(self):
        player_obj = PlayerFactory()
        arm_obj = ArmArmourFactory()

        get_resp = self.client.get(
            player_obj.detail_url,
            HTTP_AUTHORIZATION='Bearer {}'.format(self.token),
        )
        get_data = json.loads(get_resp.content.decode('utf8'))

        first_name = 'Cat'
        last_name = 'Meow'
        get_data['first_name'] = first_name
        get_data['last_name'] = last_name
        get_data['equipped_left_arm_armour_url'] = arm_obj.detail_url

        put_resp = self.client.put(
            player_obj.detail_url,
            data=json.dumps(get_data),
            content_type='application/json',
            HTTP_AUTHORIZATION='Bearer {}'.format(self.token),
        )
        put_data = json.loads(put_resp.content.decode('utf8'))

        self.assertEqual(put_resp.status_code, 202)
        self.assertEqual(put_data['first_name'], first_name)
        self.assertEqual(put_data['last_name'], last_name)
        self.assertEqual(
            put_data['equipped_left_arm_armour_url'], arm_obj.detail_url
        )

    def test_player_event_directory_factory(self):
        player_event_directory_1 = PlayerEventDirectoryFactory()
        player_event_directory_2 = PlayerEventDirectoryFactory()
        player_event_directories = [
            player_event_directory_1, player_event_directory_2,
        ]
        player_obj = PlayerFactory(
            player_event_directory=player_event_directories
        )

        get_resp = self.client.get(
            player_obj.detail_url,
            HTTP_AUTHORIZATION='Bearer {}'.format(self.token),
        )
        get_data = json.loads(get_resp.content.decode('utf8'))

        for player_event_directory in player_event_directories:
            self.assertIn(
                player_event_directory.detail_url,
                get_data['player_event_directory_urls']
            )

        self.assertEqual(len(get_data['player_event_directory_urls']), 2)

    def test_delete_player(self):
        player_obj = PlayerFactory()
        self.assertTrue(
            Player.objects.filter(id=player_obj.id, is_active=True).exists()
        )

        resp = self.client.delete(
            player_obj.detail_url,
            HTTP_AUTHORIZATION='Bearer {}'.format(self.token),
        )
        self.assertEqual(resp.status_code, 204)
        self.assertFalse(
            Player.objects.filter(id=player_obj.id, is_active=True).exists()
        )
