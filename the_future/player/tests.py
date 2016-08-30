import json

from django.test import TestCase

from player.models import Faction, Player
from utils.generic_tests import GenericDetailListTests


class PlayerTests(GenericDetailListTests, TestCase):
    model_cls = Player
    url = '/api/player/'

    def create_obj_variables(self):
        faction = Faction.objects.create(
            created_by=self.account, modified_by=self.account,
            name='First Born', description='A generic faction'
        )

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
        }

    def test_create_player(self):
        data = self.convert_fields_to_detail_url(
            self.create_obj_variables(), ['account', 'faction']
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

    # TODO
    def test_update_player(self):
        pass

    # TODO
    def test_delete_player(self):
        pass