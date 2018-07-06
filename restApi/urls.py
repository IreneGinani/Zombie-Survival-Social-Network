from django.conf.urls import url
from restApi import views

urlpatterns = [
    url(r'^api/v1/survivor/$', views.survivor_create),
    url(r'^api/v1/survivor/(?P<pk>[0-9]+)/$', views.survivor_update),
]