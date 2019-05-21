from . import *

class DataFiller:

    def fill_segment(self, segment, message_preparer):
        if segment.name == "PID":
            self.__fill_data(segment, message_preparer, PidFiller.PidFiller())
        if segment.name == "PV1":
            self.__fill_data(segment, message_preparer, Pv1Filler.Pv1Filler())

    def __fill_data(self, segment, message_preparer, filler):
        fields_count = len(segment.children)
        for pid_field in range(0, fields_count):
            filler.fill_segment(pid_field, segment, message_preparer)