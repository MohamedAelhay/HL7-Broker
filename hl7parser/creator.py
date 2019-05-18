from hl7apy.core import Message, Segment
from hl7parser.converter import Hl7FormatConverter
from hl7parser.PidCreator import PidCreator


class MessageCreator:
    def __init__(self, prepared_data=None, version=None):
        self.__prepared_data = prepared_data
        self.__message = Message(self.__prepared_data[0]['te']+'_'+self.__prepared_data[0]['scope'], version)

    def create_msh_segment(self):
        self.__message.msh.msh_6 = self.__prepared_data[0]['device']
        self.__message.msh.msh_9.msh_9_1 = self.__prepared_data[0]['te']
        self.__message.msh.msh_9.msh_9_2 = self.__prepared_data[0]['scope']
        self.__message.msh.msh_9.msh_9_3 = self.__prepared_data[0]['te']+'_'+self.__prepared_data[0]['scope']
        return self

    def create_pid_segment(self, segment_data_dict):
        pid = PidCreator().create_segment("PID", segment_data_dict)
        self.__message.add(pid)
        return self

    def create_pv1_segment(self):
        pv1 = Segment('PV1')
        pv1.pv1_1 = self.__prepared_data[2]['visit_id']
        pv1.pv1_5 = self.__prepared_data[2]['preadmit_number']
        pv1.pv1_9.pv1_9_1 = self.__prepared_data[2]['consulting_doctor_last_name']
        pv1.pv1_9.pv1_9_2 = self.__prepared_data[2]['consulting_doctor_first_name']
        self.__message.add(pv1)
        return self

    def get_hl7_message(self):
        return self.__message



