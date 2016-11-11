import json

from django.test import TestCase

from item.models import Armour
from utils.generic_tests import CreateUser


class JwtTests(TestCase, CreateUser):
    url = '/api/jwt/'

    def setUp(self):
        self.user, self.token, self.account = self.create_user()

        self.armour = Armour.objects.create(
            created_by=self.account,
            modified_by=self.account,
            name='test name',
            description='test description',
            monetary_value=100,
        )

    def test_get_and_authenticate_with_jwt(self):
        get_armour_no_auth = self.client.get(self.armour.detail_url)
        self.assertEqual(get_armour_no_auth.status_code, 401)

        get_armour_with_auth = self.client.get(
            self.armour.detail_url,
            HTTP_AUTHORIZATION='Bearer {}'.format(self.token)
        )
        self.assertEqual(get_armour_with_auth.status_code, 200)
        self.assertEqual(
            json.loads(get_armour_with_auth.content.decode('utf8'))['name'],
            self.armour.name
        )

