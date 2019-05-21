from hl7apy.core import Message, Segment


class AckMessageCreator:

    def __init__(self):
        self.__message = Message('ADT_A01', '2.5')
        self.__msa = Segment('MSA')

    def create_adt_a01_ack_message(self):
        self.__message.msh.msh_3 = 'Broker'
        self.__message.msh.msh_9.msh_9_3 = 'ACK'
        self.__message.add(self.__msa)
        return self

    def create_msa_acceptance(self):
        self.__message.msa.msa_1 = 'AA'
        return self

    def create_msa_rejection(self):
        self.__message.msa.msa_1 = 'AR'
        return self

    def get_ack_message(self):
        return self.__message
