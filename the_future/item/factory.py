from utils.factory_functions import CommonFields

from .models import BattleItem, StandardItem


class BattleItemFactory(CommonFields):
    class Meta:
        model = BattleItem


class StandardItemFactory(CommonFields):
    class Meta:
        model = StandardItem