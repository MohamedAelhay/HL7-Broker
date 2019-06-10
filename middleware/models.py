from django.db import models

# TODO: use auth_user later
class Client(models.Model):
    name = models.CharField(max_length=200)
    ip = models.CharField(max_length=15)

    def __str__(self):
        return '{}'.format(self.name)

class Device(models.Model):
    name = models.CharField(max_length=200)
    version = models.FloatField()
    ip = models.CharField(max_length=15)
    port = models.CharField(max_length=4)

class Log(models.Model):
    response =  models.CharField(max_length=200)
    time = models.DateTimeField(auto_now_add=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE) # TODO: fk on auth_user

    def __str__(self):
        return '{} {} {}'.format(self.id, ',', self.client.name)

class TriggerEvent(models.Model):
    code = models.CharField(max_length=50)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)

class Scope(models.Model):
    code = models.CharField(max_length=50)
    trigger_event = models.ForeignKey(TriggerEvent, on_delete=models.CASCADE)

class Segment(models.Model):
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    scope = models.ForeignKey(Scope, on_delete=models.CASCADE)

class Field(models.Model):
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    segment = models.ForeignKey(Segment, on_delete=models.CASCADE)
