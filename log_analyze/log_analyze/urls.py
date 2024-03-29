"""log_analyze URL Configuration

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
from django.conf.urls import include, url
from django.contrib import admin
from home.views import HomePageView
from nginx_log.views import DisplayTwoView, DisplayOneView
#from saltstack.views import SaltTestView, ajax_get_minion_statu
#from zabbix.views import ZabbixDemoView
from amazingTable.views import jqGridDemoView, serializerModule

from snippets import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    url(r'^admin/', include(admin.site.urls), name='admin'),
    url(r'^home/$', HomePageView.as_view(), name='home'),
    url(r'^dashboard/1', DisplayOneView.as_view(), name='display1'),
    url(r'^dashboard/2', DisplayTwoView.as_view(), name='display2'),
    #url(r'^saltDemo/', SaltTestView.as_view(), name='display3'),
    #url(r'^zabbixDemo/', ZabbixDemoView.as_view(), name='display4'),
    url(r'^jqGridDemo/', jqGridDemoView.as_view(), name='display5'),
    url(r'^testSerializer/', serializerModule, name='serializerModule'),
    
    # 
    url(r'^at/', include('amazingTable.urls')),
]

router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'contents', views.ContentViewSet)

urlpatterns += [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
#AJAX
#urlpatterns += [
#    url(r'^saltajaxtest/', ajax_get_minion_statu, name='ajax_get_minion_statu'),
#]