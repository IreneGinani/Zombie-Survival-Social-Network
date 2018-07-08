from django.conf.urls import url
from restApi import views

urlpatterns = [
    url(r'^api/v1/survivor/$', views.survivor_create),
    url(r'^api/v1/survivor/(?P<pk>[0-9]+)/$', views.survivor_update),
    url(r'^api/v1/inventories_items/$', views.inventories_items),
    url(r'^api/v1/survivor/report_infection/(?P<pk>[0-9]+)/$', views.report_infection),
    url(r'^api/v1/survivor/trade_items/(?P<pk>[0-9]+)/(?P<slug>[\w:-]+)/(?P<month>[0-9]+)/(?P<username>[\w:-]+)/$', views.trade_items),
    url(r'^api/v1/survivor/survivors_infected/$', views.infected_survivors_report),
    url(r'^api/v1/survivor/survivors_no_infected/$', views.no_infected_survivors_report),
    url(r'^api/v1/survivor/avg_items/$', views.avg_items),
    url(r'^api/v1/survivor/points_lost/$', views.points_lost),
    url(r'^api/v1/survivor/points_lost/(?P<pk>[0-9]+)/$', views.points_lost_survivor),

]