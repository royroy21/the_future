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


from account.api import AccountResource
from player.api import (
    ArmArmourResource,
    BackPackResource,
    BodyArmourResource,
    FactionResource,
    HeadResource,
    LegArmourResource,
    PlayerResource,
)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/jwt/', 'jwt_auth.views.obtain_jwt_token'),
]

urlpatterns += patterns('',
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
    url(r'{}'.format(HeadResource.model_cls.get_url_string()),
        include(HeadResource.urls()),
    ),
    url(r'{}'.format(LegArmourResource.model_cls.get_url_string()),
        include(LegArmourResource.urls()),
    ),
    url(r'{}'.format(PlayerResource.model_cls.get_url_string()),
        include(PlayerResource.urls()),
    ),
)