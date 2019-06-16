from middleware.models import Log
import datetime

class Logger:
    @staticmethod
    def log(device , client, status):
        time = datetime.datetime.strftime(datetime.datetime.now(),"%Y-%m-%dT%H:%M:%S")
        Log.objects.create(device = device, time= time, client_id= client.id, status = status)


