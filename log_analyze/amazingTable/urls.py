from django.conf.urls import url
from amazingTable import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^contents/$', views.ContentList.as_view()),
    url(r'^contents/(?P<pk>[0-9]+)/$', views.ContentDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)