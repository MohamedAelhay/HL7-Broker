from django.shortcuts import render
from hl7apy.mllp import AbstractHandler, AbstractErrorHandler, UnsupportedMessageType
from hl7apy.parser import parse_message

# Create your views here.

class PDQHandler(AbstractHandler):
    def reply(self):
        print("I'm Listening... ")
        msg = parse_message(self.incoming_message)
        # Do Something with the Message

        res = Message('RSP_K21')
        # Populate the Message

        return res.to_mllp()


class ErrorHandler(AbstractErrorHandler):
    def reply(self):
        if isinstance(self.exc, UnsupportedMessageType):
            # Return custom response for unsupported message
            print("Unsupported Message Type")
        else:
            # Return custom response for general errors
            print("General Error")
