from django.shortcuts import render
from hl7apy.mllp import AbstractHandler, AbstractErrorHandler, UnsupportedMessageType
from hl7apy.core import Message
from hl7apy.parser import parse_message

# Create your views here.

class PDQHandler(AbstractHandler):
    def reply(self):
        print("I'm Listening... ")
        msg = parse_message(self.incoming_message)
        # Do Something with the Message

        res = Message('RSP_K21')
        # Populate the Message
        res.msh = "MSH|^~\&|HOSPMPI|HOSP|CLINREG|WESTCLIN|199912121135-0600||RSP^K21^RSP_K21|1|D|2.5|\r"
        res.msa = "MSA|AA|8699|\r"
        res.qak = "QAK|111069|OK|Q21^Get Person Demographics^HL7nnn|1|\r"
        res.qpd = "QPD|Q21^Get Person Demographics^HL7nnn|111069|112234^^^GOOD HEALTH HOSPITAL|^^^ GOOD HEALTH HOSPITAL~^^^SOUTH LAB|\r"
        res.pid = "PID|||112234^^^GOOD HEALTH HOSPITAL~98223^^^SOUTH LAB||Everyman^Adam||19600614|M||C|2101 Webster # 106^^Oakland^CA^94612|\r"
        res.qri = "QRI|100|"
        
        print(res.children)
        res.to_mllp()
        return res.to_mllp()


class ErrorHandler(AbstractErrorHandler):
    def reply(self):
        if isinstance(self.exc, UnsupportedMessageType):
            # Return custom response for unsupported message
            print("Unsupported Message Type")
        else:
            # Return custom response for general errors
            print(self.exc)
            print("General Error")


def handlers():
    return {
        'QBP^Q22^QBP_Q21': (PDQHandler,),
        'ADT^A01^ADT_A01': (PDQHandler,),
        'ERR': (ErrorHandler,)
    }
