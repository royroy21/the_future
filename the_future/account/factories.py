import factory

from django.contrib.auth.models import User

from .models import Account


class UserFactory(factory.django.DjangoModelFactory):
    username = factory.Sequence(lambda n: 'user_{0}'.format(n))
    is_active = True
    is_superuser = False
    is_staff = False
    password = 'Pa$$word'

    class Meta:
        model = User


class AccountFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)

    class Meta:
        model = Account