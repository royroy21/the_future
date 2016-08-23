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
]

urlpatterns += patterns('',
    url(r'api/arm-armour/', include(ArmArmourResource.urls())),
    url(r'api/back-pack/', include(BackPackResource.urls())),
    url(r'api/body-armour/', include(BodyArmourResource.urls())),
    url(r'api/faction/', include(FactionResource.urls())),
    url(r'api/head/', include(HeadResource.urls())),
    url(r'api/leg-armour/', include(LegArmourResource.urls())),
    url(r'api/player/', include(PlayerResource.urls())),
)