import json

from django.test import TestCase

from account.models import Account


class AccountTests(TestCase):
    url = '/api/account/'
    jwt_api_url = '/api/jwt/'

    def _create_user_through_api(self, username, password_1, password_2):
        data = {
            'username': username,
            'password_1': password_1,
            'password_2': password_2,
        }
        return self.client.post(
            self.url, data=json.dumps(data), content_type='application/json'
        )

    def test_create(self):
        username = 'mr_cat'
        password = 'Pa$$w0rD'
        resp = self._create_user_through_api(username, password, password)
        self.assertEqual(resp.status_code, 201)

        resp_data = json.loads(resp.content.decode('utf8'))
        self.assertEqual(resp_data['username'], username)

        self.assertEqual(
            Account.objects.filter(
                user__username=username, user__is_active=True
            ).count(), 1
        )

        # get jwt
        jwt_data = {
            'username': username,
            'password': password,
        }
        jwt_resp = self.client.post(
            self.jwt_api_url,
            json.dumps(jwt_data),
            content_type='application/json',
        )
        self.assertTrue(json.loads(jwt_resp.content.decode('utf8'))['token'])

    def test_create_with_mismatched_passwords(self):
        username = 'mr_dog'
        resp = self._create_user_through_api('mr_dog', 'Pa$$w0rD', 'Pa$$w0Dx')
        self.assertEqual(resp.status_code, 400)

        self.assertEqual(
            Account.objects.filter(
                user__username=username, user__is_active=True
            ).count(), 0
        )