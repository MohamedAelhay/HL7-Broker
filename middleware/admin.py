from django.contrib import admin
from .models import Log,Client
# Register your models here.

class CustomLog(admin.ModelAdmin):
    list_display = ('id', 'client', 'response', 'time')

admin.site.register(Log,CustomLog)
