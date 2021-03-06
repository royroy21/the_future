"""mc_notey URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import patterns, url, include
from django.contrib import admin
from jwt_auth.views import obtain_jwt_token


from account.api import AccountResource
from combat_simulator.api import CombatRequestResource
from hero.api import HeroResource
from item.api import (
    ArmourResource,
    AbilityResource,
    ItemResource,
    ShieldResource,
    WeaponResource,
)
from player.api import FactionResource, PlayerResource


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/jwt/', obtain_jwt_token),
]

urlpatterns += patterns('',
    url(r'{}'.format(AccountResource.model_cls.get_url_string()),
        include(AccountResource.urls()),
    ),
    url(r'{}'.format(HeroResource.model_cls.get_url_string()),
        include(HeroResource.urls()),
    ),
    url(r'{}'.format(ArmourResource.model_cls.get_url_string()),
        include(ArmourResource.urls()),
    ),
    url(r'{}'.format(AbilityResource.model_cls.get_url_string()),
        include(AbilityResource.urls()),
    ),
    url(r'{}'.format(ItemResource.model_cls.get_url_string()),
        include(ItemResource.urls()),
    ),
    url(r'{}'.format(FactionResource.model_cls.get_url_string()),
        include(FactionResource.urls()),
    ),
    url(r'{}'.format(ShieldResource.model_cls.get_url_string()),
        include(ShieldResource.urls()),
    ),
    url(r'{}'.format(WeaponResource.model_cls.get_url_string()),
        include(WeaponResource.urls()),
    ),
    url(r'{}'.format(PlayerResource.model_cls.get_url_string()),
        include(PlayerResource.urls()),
    ),
    url(r'{}'.format(CombatRequestResource.model_cls.get_url_string()),
        include(CombatRequestResource.urls()),
    ),
)