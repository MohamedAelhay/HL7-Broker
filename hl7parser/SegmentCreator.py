from hl7apy.core import Segment
from hl7parser.ISegment import ISegment
from hl7parser.FieldsDataType import *


class SegmentCreator(ISegment):

    def create_segment(self, segment_name, segment_data_dict):
        segment = Segment(segment_name)

        for field in segment_data_dict:
            segment.add_field(field)

        for field in segment.children:
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
            if field.datatype == "DLD":
                DldCreator.DldCreator().create_field(field)
            if field.datatype == "XCN":
                XcnCreator.XcnCreator().create_field(field)
            if field.datatype == "PL":
                PlCreator.PlCreator().create_field(field)
            if field.datatype == "FC":
                FcCreator.FcCreator().create_field(field)
        return segment
