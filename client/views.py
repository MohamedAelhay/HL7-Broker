from django.shortcuts import render
from middleware.models import Log

# Create your views here.

def getUserLogs(request):
    userLogs = Log.objects.filter(client=request.user.id)
    context = {"logs" : userLogs}
    return render(request,'dashboard/index.html', context)
