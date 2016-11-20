import json

from django.test import TestCase

from hero.factories import HeroFactory


class TestCombatRequest(TestCase):
    url = '/api/combat-request/'

    def setUp(self):
        self.hero_1 = HeroFactory()
        self.hero_1_jwt = self.hero_1.player.get_jwt()
        self.hero_2 = HeroFactory()
        self.hero_2_jwt = self.hero_2.player.get_jwt()

    def _initiate_combat(self):
        data = {
            'initiating_player_url': self.hero_1.player.detail_url,
            'waiting_for_player_url': self.hero_2.player.detail_url,
        }
        resp = self.client.post(
            self.url, data=json.dumps(data),
            content_type='application/json',
            HTTP_AUTHORIZATION='Bearer {}'.format(self.hero_1_jwt)
        )
        resp_data = json.loads(resp.content.decode('utf8'))

        self.assertEqual(
            resp_data['initiating_player_url'], self.hero_1.player.detail_url)
        self.assertEqual(
            resp_data['waiting_for_player_url'], self.hero_2.player.detail_url)
        self.assertFalse(resp_data['combat_ready'])
        self.assertTrue(resp_data['is_active'])
        self.assertEqual(resp_data['created_by_url'],
                         self.hero_1.player.account.detail_url)
        self.assertEqual(resp_data['modified_by_url'],
                         self.hero_1.player.account.detail_url)

        # test request combat call
        for params in [None, {'player_id': self.hero_1.player.id}]:
            resp_combat_data = self._get_combat_requests_available(
                self.hero_1_jwt, params=params)['objects'][0]

            self.assertFalse(resp_combat_data['combat_ready'])
            self.assertEqual(resp_combat_data['created_by_url'],
                             self.hero_1.player.account.detail_url)
            self.assertEqual(resp_combat_data['modified_by_url'],
                             self.hero_1.player.account.detail_url)
            self.assertEqual(resp_combat_data['initiating_player_url'],
                             self.hero_1.player.detail_url)
            self.assertTrue(resp_combat_data['is_active'])
            self.assertFalse(resp_combat_data['points'])
            self.assertEqual(resp_combat_data['waiting_for_player_url'],
                             self.hero_2.player.detail_url)

    def _get_combat_requests_available(self, jwt, params=None):
        if not params:
            params = {}

        resp_combat = self.client.get(
            self.url + 'available/', params,
            HTTP_AUTHORIZATION='Bearer {}'.format(jwt))
        self.assertEqual(resp_combat.status_code, 200)
        return resp_combat.json()

    def test_init_player_tries_to_combat_ready_a_combat_request(self):
        self._initiate_combat()

        resp_combat_data = self._get_combat_requests_available(self.hero_1_jwt)
        data = resp_combat_data['objects'][0]
        data['combat_ready'] = True

        resp = self.client.put(
            data['self'], data=json.dumps(data),
            content_type='application/json',
            HTTP_AUTHORIZATION='Bearer {}'.format(self.hero_1.player.get_jwt())
        )
        self.assertEqual(resp.status_code, 400)
        self.assertEqual(
            resp.json()['error'], 'only "waiting for player" can ready combat')

    def test_reply_negative_to_initiate_combat(self):
        self._initiate_combat()

        data = self._get_combat_requests_available(
            self.hero_2_jwt)['objects'][0]

        resp = self.client.put(
            data['self'], data=json.dumps(data),
            content_type='application/json',
            HTTP_AUTHORIZATION='Bearer {}'.format(self.hero_2.player.get_jwt())
        )
        resp_data = json.loads(resp.content.decode('utf8'))
        self.assertFalse(resp_data['is_active'])

        # test combat request doesn't return for either player
        self.assertFalse(
            self._get_combat_requests_available(self.hero_2_jwt)['objects'])
        self.assertFalse(
            self._get_combat_requests_available(self.hero_1_jwt)['objects'])

    def test_reply_positive_to_initiate_combat(self):
        self._initiate_combat()

        resp_combat_data = self._get_combat_requests_available(
            self.hero_2_jwt, {'player_id': self.hero_2.player.id})

        data = resp_combat_data['objects'][0]
        data['combat_ready'] = True

        resp = self.client.put(
            data['self'], data=json.dumps(data),
            content_type='application/json',
            HTTP_AUTHORIZATION='Bearer {}'.format(self.hero_2.player.get_jwt())
        )
        resp_data = json.loads(resp.content.decode('utf8'))

        self.assertEqual(
            resp_data['initiating_player_url'], self.hero_1.player.detail_url)
        self.assertEqual(
            resp_data['waiting_for_player_url'], self.hero_2.player.detail_url)
        self.assertTrue(resp_data['combat_ready'])
        self.assertTrue(resp_data['is_active'])

        # test combat is also available for player 1
        resp_combat_data = self._get_combat_requests_available(self.hero_1_jwt)
        self.assertTrue(resp_combat_data['objects'][0]['combat_ready'])