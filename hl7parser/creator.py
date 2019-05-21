from hl7apy.core import Message, Segment
from hl7parser.converter import Hl7FormatConverter
from hl7parser.SegmentCreator import SegmentCreator


class MessageCreator:
    def __init__(self, prepared_data=None, version=None):
        self.__prepared_data = prepared_data
        self.__message = Message(self.__prepared_data[0]['SCOPE']+'_'+self.__prepared_data[0]['TE'], version)

    def create_msh_segment(self):
        self.__message.msh.msh_6 = self.__prepared_data[0]['DEVICE']
        self.__message.msh.msh_9.msh_9_1 = self.__prepared_data[0]['SCOPE']
        self.__message.msh.msh_9.msh_9_2 = self.__prepared_data[0]['TE']
        self.__message.msh.msh_9.msh_9_3 = self.__prepared_data[0]['SCOPE']+'_'+self.__prepared_data[0]['TE']
        return self

    def create_pid_segment(self, segment_data_dict):
        pid = SegmentCreator().create_segment("PID", segment_data_dict)
        self.__message.add(pid)
        return self

    def create_pv1_segment(self, segment_data_dict):
        pv1 = SegmentCreator().create_segment("PV1", segment_data_dict)
        self.__message.add(pv1)
        return self

    def get_hl7_message(self):
        return self.__message



