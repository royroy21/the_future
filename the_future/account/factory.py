import factory

from django.contrib.auth.models import User

from .models import Account


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: 'user_{0}'.format(n))
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.Sequence(lambda n: 'user_{0}@example.com'.format(n))
    is_active = True
    is_superuser = False
    is_staff = False
    password = 'Pa$$word'


class AccountFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Account

    user = factory.SubFactory(UserFactory)