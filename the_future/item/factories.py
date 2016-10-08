from utils.factory_functions import CommonFields

from .models import BattleItem, ShieldItem, StandardItem


class StandardItemFactory(CommonFields):
    class Meta:
        model = StandardItem


class BattleItemFactory(CommonFields):
    class Meta:
        model = BattleItem


class ShieldItemFactory(CommonFields):
    class Meta:
        model = ShieldItem