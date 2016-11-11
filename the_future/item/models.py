from utils.generic_models import CommonFields, ModifierField, MonetaryField
from django.db import models


class StandardItem(CommonFields, ModifierField, MonetaryField):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Item(StandardItem):
    pass


class Weapon(StandardItem):
    pass


class Shield(StandardItem):
    pass


class Armour(StandardItem):
    pass


class Ability(StandardItem):
    pass