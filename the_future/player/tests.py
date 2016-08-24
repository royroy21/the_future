import json

from django.contrib.auth.models import User
from django.test import TestCase

from account.models import Account
from player.models import LegArmour


class LegArmourTests(TestCase):

    url = '/api/leg-armour/'

    def setUp(self):
        user = User.objects.create(
            username='cat', password='password')
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

    def _test_fields(self, data):
        self.assertEquals(data['name'], self.leg_armour.name)
        self.assertEquals(data['description'], self.leg_armour.description)
        self.assertEquals(data['amount_of_items'],
                          str(self.leg_armour.amount_of_items))
        self.assertEquals(data['health'], str(self.leg_armour.health))
        self.assertEquals(data['value'], str(self.leg_armour.value))
        self.assertEquals(data['created_by'], self.account.detail_url)
        self.assertEquals(data['modified_by'], self.account.detail_url)

    def test_detail(self):
        resp = self.client.get('{}{}/'.format(self.url, self.leg_armour.id))

        self.assertEqual(resp.status_code, 200)
        resp_data = json.loads(resp.content.decode('utf8'))

        self._test_fields(resp_data)

    def test_list(self):
        resp = self.client.get(self.url)

        self.assertEqual(resp.status_code, 200)
        resp_data = json.loads(resp.content.decode('utf8'))['objects'][0]

        self._test_fields(resp_data)