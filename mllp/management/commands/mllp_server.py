from django.core.management.base import BaseCommand
from mllp.views import PDQHandler, ErrorHandler, handlers
from hl7apy.mllp import MLLPServer

class Command(BaseCommand):
    help = "Start MLLP Server"

    def handle(self, *args, **kwargs):
        server = MLLPServer('localhost', 2575, handlers())
        server.serve_forever()
        