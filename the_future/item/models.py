from django.contrib.contenttypes.fields import GenericRelation

from utils.generic_models import CommonFields


class StandardItem(CommonFields):
    events = GenericRelation('Event', null=True, blank=True)


class BattleItem(StandardItem):
    pass


class ShieldItem(StandardItem):
    pass