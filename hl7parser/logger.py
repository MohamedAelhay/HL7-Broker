from middleware.models import Log
import datetime

class Logger:
    @staticmethod
    def log(response , client):
        time = datetime.datetime.strftime(datetime.datetime.now(),"%Y-%m-%dT%H:%M:%S")
        Log.objects.create(response = response, time= time, client_id= client)


