from django.contrib import admin
# from jet.filters import DateRangeFilter
from .models import Log,Client
# Register your models here.

class CustomLog(admin.ModelAdmin):
    list_display = ('id', 'client', 'device', 'status', 'time')
    list_filter = (
        'time', 'device', 'status'
    )

admin.site.register(Log,CustomLog)
