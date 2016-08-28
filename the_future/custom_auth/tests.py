import json

from django.test import TestCase

from player.models import LegArmour
from utils.generic_tests import CreateUser


class JwtTests(TestCase, CreateUser):
    url = '/api/jwt/'

    def setUp(self):
        self.user, self.token, self.account = self.create_user()

        self.leg_armour = LegArmour.objects.create(
            created_by=self.account,
            modified_by=self.account,
            name='test name',
            description='test description',
            amount_of_items=2,
            health=9,
            value=100,
        )

    def test_get_and_authenticate_with_jwt(self):
        get_leg_no_auth = self.client.get(self.leg_armour.detail_url)
        self.assertEqual(get_leg_no_auth.status_code, 401)

        get_leg_with_auth = self.client.get(
            self.leg_armour.detail_url,
            HTTP_AUTHORIZATION='Bearer {}'.format(self.token)
        )

        self.assertEqual(get_leg_with_auth.status_code, 200)
        self.assertEqual(
            json.loads(get_leg_with_auth.content.decode('utf8'))['name'],
            self.leg_armour.name
        )

