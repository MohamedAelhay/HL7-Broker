from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import hashlib


# TODO: use auth_user later
class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ip = models.CharField(max_length=15 , default='127.0.0.1')
    key = models.CharField(max_length=200)

    def __str__(self):
        return '{}'.format(self.ip)

class Device(models.Model):
    name = models.CharField(max_length=200)
    version = models.FloatField()
    ip = models.CharField(max_length=15)
    port = models.CharField(max_length=4)

class Log(models.Model):
    device =  models.CharField(max_length=200)
    status = models.CharField(max_length=50, default = "Success")
    time = models.DateTimeField(auto_now_add=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE) # TODO: fk on auth_user

    def __str__(self):
        return '{} {} {}'.format(self.id, ',', self.client.ip)

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


@receiver(post_save, sender=User)
def create_user_client(sender, instance, created, **kwargs):
    if created:
        key = encrypt_string(instance.email)
        Client.objects.create(user=instance , key=key)

@receiver(post_save, sender=User)
def save_user_client(sender, instance, **kwargs):
    instance.client.save()


def encrypt_string(hash_string):
    sha_signature = hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature
