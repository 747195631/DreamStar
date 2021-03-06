# coding=utf-8
###########################################
# File: parameters_config_urls.py
# Desc: 参数设置控制层
# Author: 张羽锋
# History: 2016/01/02 张羽锋 新建
###########################################
"""DreamStar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url

urlpatterns = [
    url(r'^crmmock/ytdycCrm', "totest.views.ytdyc_crm"),
    url(r'^crmmock/oyjtCrm/(.+)', "totest.views.oyjt_crm"),
    url(r'^crmmock/crmMockInterface', "totest.views.crmmock_interface"),
    url(r'^crmmock/crmMockPayDataJsonResponse.json', "totest.views.crmmock_paydata_json_response"),
    url(r'^crmmock/queryCrmCardno.json', "totest.views.query_cardno"),
    url(r'^crmmock/crmDataSetting', "totest.views.crmdata_setting"),
    url(r'^crmmock/crmSettingsPage', "totest.views.crm_settings_page"),
    url(r'^crmmock/crmSettingsJsonResponse.json', "totest.views.crm_settings_json_response"),
    url(r'^crmmock/crmSetting', "totest.views.crm_setting"),
    url(r'^settings/interfaceSettingsTreegrid$', 'totest.views.interface_settings_treegrid'),
    url(r'^settings/interfaceSettingsJsonResponse.json$', 'totest.views.interface_settings_json_response'),
    url(r'^settings/interfaceSetting$', 'totest.views.interface_setting'),
]
