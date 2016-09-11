from restless.exceptions import BadRequest, NotFound
from restless.preparers import FieldsPreparer

from utils.generic_resources import GenericReadOnlyResource

from .forms import AccountCreateForm
from .models import Account


class AccountResource(GenericReadOnlyResource):
    model_cls = Account

    preparer = FieldsPreparer(fields={'username': 'user.username'})

    def is_authenticated(self):
        """We don't test for authentication on create
        """
        if not self.data:
            return True

        user_is_updating_self = self.request.user.id == self.data.id
        return (self.request.user.is_authenticated()
                and user_is_updating_self)

    def reference_object(self, pk):
        try:
            return self.model_cls.objects.get(id=pk, is_active=True)
        except self.model_cls.DoesNotExist:
            raise NotFound

    def create(self):
        form = AccountCreateForm(data=self.data)
        if form.is_valid():
            return form.save()
        raise BadRequest(form.errors.as_json())

    # TODO - create update form + logic
    def update(self, pk):
        pass

    def delete(self, pk):
        obj = self.reference_object(pk)
        obj.is_active = False
        obj.save()