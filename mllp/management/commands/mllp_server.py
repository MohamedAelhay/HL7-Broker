from django.core.management.base import BaseCommand
from mllp.views import PDQHandler, ErrorHandler
from hl7apy.mllp import MLLPServer

class Command(BaseCommand):
    help = "Start MLLP Server"

    handlers = {
        'QBP^Q22^QBP_Q21': (PDQHandler,),
        'ERR': (ErrorHandler,)
    }

    def handle(self, *args, **kwargs):
        server = MLLPServer('localhost', 2575, self.handlers)
        server.serve_forever()
        