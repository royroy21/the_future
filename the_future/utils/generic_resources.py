from restless.dj import DjangoResource


COMMON_PREPARE_FIELDS = {
    'created_by': 'created_by.username',
    'modified_by': 'modified_by.username',
    'created': 'created',
    'is_active': 'is_active'
}


class GenericReadOnlyResource(DjangoResource):
    model_cls = None

    def list(self):
        return self.model_cls.objects.filter(is_active=True)

    def detail(self, pk):
        return self.model_cls.objects.get(id=pk, is_active=True)


class GenericCrudResource(GenericReadOnlyResource):

    def create(self):
        pass

    def update(self, pk):
        pass

    def delete(self, pk):
        pass