from django.contrib import admin
from django.conf.urls import url
from client import views

urlpatterns = [
    url(r'^dashboard/$',views.index,name="dashboard"),
    url(r'^dashboard/cancel-subscription$', views.cancel_subscription, name="client_cancel_subscription"),
    url(r'^dashboard/add_bookmark$' , views.add_bookmark_view , name='add_bookmark'),
    url(r'^dashboard/remove_bookmark$', views.remove_bookmark_view, name='remove_bookmark'),
    url(r'^dashboard/HL7-Broker/logs', views.changelist , name='logs'),
    url(r'^dashboard/HL7-Broker', views.app_index , name='HL7-Broker'),

]