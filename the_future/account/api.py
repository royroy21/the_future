from restless.preparers import FieldsPreparer

from utils.generic_resources import GenericReadOnlyResource

from .models import Account


class AccountResource(GenericReadOnlyResource):
    model_cls = Account
    preparer = FieldsPreparer(fields={'user': 'user.username'})