from django.contrib import admin
from django.conf.urls import url
from middleware import views

urlpatterns = [
    url(r'^parse/$',views.parse_request,name="request"),
    url(r'^device/(?P<pk>[0-9]+)$', views.device_details,name="device_details")
]
