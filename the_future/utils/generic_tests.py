import json

from django.contrib.auth.models import User

from account.models import Account
from utils.url_to_object import url_to_object


class CreateUser(object):

    jwt_api_url = '/api/jwt/'
    username = 'Cat'
    password = 'CatNip1980'

    def create_user(self, is_superuser=False):
        create_user_params = {
            'username': self.username,
            'password': self.password
        }
        if is_superuser:
            create_user_params['is_superuser'] = True

        user = User.objects.create_user(**create_user_params)
        account = Account.objects.create(user=user)

        return user, self._get_jwt(), account

    def _get_jwt(self):
        data = {
            'username': self.username,
            'password': self.password,
        }
        resp = self.client.post(
            self.jwt_api_url,
            json.dumps(data),
            content_type='application/json',
        )
        return json.loads(resp.content.decode('utf8'))['token']


class GenericDetailListTests(CreateUser):
    url = None
    model_cls = None

    def setUp(self):
        self.user, self.token, self.account = self.create_user()

        create_vars = self.create_obj_variables()
        create_vars.update(
            {'created_by': self.account, 'modified_by': self.account}
        )
        self.test_obj = self.model_cls.objects.create(**create_vars)

    def create_obj_variables(self):
        pass

    def convert_fields_to_detail_url(self, data, field_array):
        """Converts fields in data so to be JSON friendly
        """
        for field in field_array:
            data['{}_url'.format(field)] = data[field].detail_url
            del data[field]

        return data

    def _test_fields(self, data):
        for k, v in data.items():
            try:
                self.assertEquals(str(v), str(getattr(self.test_obj, k)))
            except (AssertionError, AttributeError):
                self.assertEquals(
                    v, getattr(self.test_obj, k.strip('_url')
                    ).detail_url)

    def test_detail(self):
        resp = self.client.get(
            '{}{}/'.format(self.url, self.test_obj.id),
            HTTP_AUTHORIZATION='Bearer {}'.format(self.token)
        )

        self.assertEqual(resp.status_code, 200)
        resp_data = json.loads(resp.content.decode('utf8'))

        self._test_fields(resp_data)

    def test_list(self):
        resp = self.client.get(
            self.url, HTTP_AUTHORIZATION='Bearer {}'.format(self.token)
        )

        self.assertEqual(resp.status_code, 200)
        resp_data = json.loads(resp.content.decode('utf8'))['objects'][0]

        self._test_fields(resp_data)

    def test_url_to_object(self):
        new_obj = url_to_object(self.test_obj.detail_url)
        self.assertEqual(new_obj, self.test_obj)
