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
from armour.api import (
    ArmArmourResource,
    BackPackResource,
    BodyArmourResource,
    HeadArmourResource,
    LegArmourResource,
)
from event.api import (
    EventResource,
    PlayerEventTitleResource,
    PlayerEventValueResource,
    PlayerEventDirectoryResource,
)
from item.api import (
    BattleItemResource, ShieldItemResource, StandardItemResource,
)
from player.api import FactionResource, PlayerResource


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/jwt/', obtain_jwt_token),
]

urlpatterns += patterns('',
    url(r'{}'.format(EventResource.model_cls.get_url_string()),
        include(EventResource.urls()),
    ),
    url(r'{}'.format(PlayerEventTitleResource.model_cls.get_url_string()),
        include(PlayerEventTitleResource.urls()),
    ),
    url(r'{}'.format(PlayerEventValueResource.model_cls.get_url_string()),
        include(PlayerEventValueResource.urls()),
    ),
    url(r'{}'.format(PlayerEventDirectoryResource.model_cls.get_url_string()),
        include(PlayerEventDirectoryResource.urls()),
    ),
    url(r'{}'.format(AccountResource.model_cls.get_url_string()),
        include(AccountResource.urls()),
    ),
    url(r'{}'.format(ArmArmourResource.model_cls.get_url_string()),
        include(ArmArmourResource.urls()),
    ),
    url(r'{}'.format(BackPackResource.model_cls.get_url_string()),
        include(BackPackResource.urls()),
    ),
    url(r'{}'.format(BodyArmourResource.model_cls.get_url_string()),
        include(BodyArmourResource.urls()),
    ),
    url(r'{}'.format(FactionResource.model_cls.get_url_string()),
        include(FactionResource.urls()),
    ),
    url(r'{}'.format(HeadArmourResource.model_cls.get_url_string()),
        include(HeadArmourResource.urls()),
    ),
    url(r'{}'.format(LegArmourResource.model_cls.get_url_string()),
        include(LegArmourResource.urls()),
    ),
    url(r'{}'.format(PlayerResource.model_cls.get_url_string()),
        include(PlayerResource.urls()),
    ),
    url(r'{}'.format(BattleItemResource.model_cls.get_url_string()),
        include(BattleItemResource.urls()),
    ),
    url(r'{}'.format(ShieldItemResource.model_cls.get_url_string()),
        include(ShieldItemResource.urls()),
    ),
    url(r'{}'.format(StandardItemResource.model_cls.get_url_string()),
        include(StandardItemResource.urls()),
    ),
)