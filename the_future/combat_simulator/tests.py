import json

from django.test import TestCase

from hero.factories import HeroFactory
from utils.generic_tests import CreateUser


class TestCombatRequest(TestCase, CreateUser):
    url = '/api/combat-request/'

    def setUp(self):
        self.user, self.token, self.account = self.create_user()

        self.hero_1 = HeroFactory()
        self.hero_2 = HeroFactory()

    def _initiate_combat(self):
        data = {
            'initiating_player_url': self.hero_1.player.detail_url,
            'initiating_hero_url': self.hero_1.detail_url,
            'waiting_for_player_url': self.hero_2.player.detail_url,
        }
        resp = self.client.post(
            self.url, data=json.dumps(data),
            content_type='application/json',
            HTTP_AUTHORIZATION='Bearer {}'.format(self.token)
        )
        resp_data = json.loads(resp.content.decode('utf8'))

        self.assertEqual(
            resp_data['initiating_player_url'], self.hero_1.player.detail_url)
        self.assertEqual(
            resp_data['initiating_hero_url'], self.hero_1.detail_url)
        self.assertEqual(
            resp_data['waiting_for_player_url'], self.hero_2.player.detail_url)
        self.assertFalse(resp_data['waiting_for_hero_url'])
        self.assertFalse(resp_data['combat_ready'])
        self.assertTrue(resp_data['is_active'])

        return resp_data

    def test_reply_positive_to_initiate_combat(self):
        data = self._initiate_combat()
        data['waiting_for_hero_url'] = self.hero_2.detail_url

        resp = self.client.put(
            data['self'], data=json.dumps(data),
            content_type='application/json',
            HTTP_AUTHORIZATION='Bearer {}'.format(self.token)
        )
        resp_data = json.loads(resp.content.decode('utf8'))

        self.assertEqual(
            resp_data['initiating_player_url'], self.hero_1.player.detail_url)
        self.assertEqual(
            resp_data['initiating_hero_url'], self.hero_1.detail_url)
        self.assertEqual(
            resp_data['waiting_for_player_url'], self.hero_2.player.detail_url)
        self.assertEqual(
            resp_data['waiting_for_hero_url'], self.hero_2.detail_url)
        self.assertTrue(resp_data['combat_ready'])
        self.assertTrue(resp_data['is_active'])