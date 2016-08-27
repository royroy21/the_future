import json

from django.contrib.auth.models import User
from django.test import TestCase

from account.models import Account
from player.models import LegArmour


class JwtTests(TestCase):
    url = '/api/jwt/'

    def setUp(self):
        self.username = 'Cat'
        self.password = 'CatNip1980'

        user = User.objects.create_user(
            username=self.username, password=self.password)
        self.account = Account.objects.create(user=user)

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
        data = {
            'username': self.username,
            'password': self.password,
        }
        resp = self.client.post(
            self.url,
            json.dumps(data),
            content_type='application/json',
        )
        self.assertEqual(resp.status_code, 200)
        token = json.loads(resp.content.decode('utf8'))['token']

        get_leg_no_auth = self.client.get(self.leg_armour.detail_url)
        self.assertEqual(get_leg_no_auth.status_code, 401)

        get_leg_with_auth = self.client.get(
            self.leg_armour.detail_url,
            HTTP_AUTHORIZATION='Bearer {}'.format(token)
        )

        self.assertEqual(get_leg_with_auth.status_code, 200)
        self.assertEqual(
            json.loads(get_leg_with_auth.content.decode('utf8'))['name'],
            self.leg_armour.name
        )
