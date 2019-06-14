from django.conf.urls import url
from django.urls import path

from memberships import views

urlpatterns = [
    url(r'^$', views.selectMemberShip,name="selectMemberShip"),
    url(r'^payment/$', views.payment, name='payment'),
    path('update-transactions/<subscription_id>/',
             views.updateTransactionRecords, name='update-transactions'),
]