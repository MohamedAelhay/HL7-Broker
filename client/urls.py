from django.contrib import admin
from django.conf.urls import url
from client import views

urlpatterns = [
    url(r'^dashboard/$',views.getUserLogs,name="dashboard"),
]