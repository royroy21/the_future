from django.db import models

from utils.generic_models import CommonFields


class Armour(CommonFields):
    name = models.CharField(max_length=255)
    description = models.TextField()
    health = models.DecimalField(max_digits=2, decimal_places=0)
    value = models.DecimalField(max_digits=7, decimal_places=0)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class ArmArmour(Armour):
    pass


class HeadArmour(Armour):
    pass


class LegArmour(Armour):
    pass


class BodyArmour(Armour):
    pass


class BackPack(Armour):
    pass