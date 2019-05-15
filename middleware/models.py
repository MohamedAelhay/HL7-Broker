from django.db import models

# TODO: use auth_user later
class Client(models.Model):
    name = models.CharField(max_length=200)
    ip = models.CharField(max_length=15)

class Device(models.Model):
    name = models.CharField(max_length=200)
    version = models.FloatField()

class Log(models.Model):
    response =  models.CharField(max_length=200)
    time = models.DateTimeField(auto_now_add=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE) # TODO: fk on auth_user

class TriggerEvent(models.Model):
    name = models.CharField(max_length=50)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)

class Scope(models.Model):
    name = models.CharField(max_length=50)
    trigger_event = models.ForeignKey(TriggerEvent, on_delete=models.CASCADE)

class Segment(models.Model):
    name = models.CharField(max_length=50)
    scope = models.ForeignKey(Scope, on_delete=models.CASCADE)

class Field(models.Model):
    name = models.CharField(max_length=50)
    segment = models.ForeignKey(Segment, on_delete=models.CASCADE)
