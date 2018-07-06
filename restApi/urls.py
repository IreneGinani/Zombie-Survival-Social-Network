from django.conf.urls import url
from survivor import views

urlpatterns = [
    url(r'^survivor/$', views.survivor_create),
    url(r'^survivor/(?P<pk>[0-9]+)/$', views.survivor_update),
]