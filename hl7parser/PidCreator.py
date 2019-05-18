from hl7apy.core import Segment
from hl7parser.ISegment import ISegment
from hl7parser.FieldsDataType import *


class PidCreator(ISegment):

    def create_segment(self, pid_segment, segment_data_dict):
        pid = Segment("PID")

        for field in segment_data_dict:
            pid.add_field(field)

        for field in pid.children:
            if field.datatype == "CX":
                CxCreator.CxCreator().create_field(field)
            if field.datatype == "XPN":
                XpnCreator.XpnCreator().create_field(field)
            if field.datatype == "TS":
                TsCreator.TsCreator().create_field(field)
            if field.datatype == "XAD":
                XadCreator.XadCreator().create_field(field)
            if field.datatype == "DLN":
                DlnCreator.DlnCreator().create_field(field)
            if field.datatype == "HD":
                HdCreator.HdCreator().create_field(field)
            if field.datatype == "CWE":
                CweCreator.CweCreator().create_field(field)
            if field.datatype == "CE":
                CeCreator.CeCreator().create_field(field)
            if field.datatype == "XTN":
                XtnCreator.XtnCreator().create_field(field)
            if field.datatype == "NM":
                NmCreator.NmCreator().create_field(field)
        return pid
