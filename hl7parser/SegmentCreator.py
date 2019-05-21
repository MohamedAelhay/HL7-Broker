from hl7apy.core import Segment
from hl7parser.ISegment import ISegment
from hl7parser import helper


class SegmentCreator(ISegment):

    def create_segment(self, segment_name, segment_data_dict):
        segment = Segment(segment_name)

        for field in segment_data_dict:
            segment.add_field(field)
        segment_keys_list = list(segment_data_dict.keys())

        for field_name in segment_keys_list:
            if isinstance(helper.get_data_from_dict_key(segment_data_dict, field_name), dict):
                for comp in helper.get_data_from_dict_key(segment_data_dict, field_name).keys():
                    segment.children[segment_keys_list.index(field_name)].add_component(comp)
        return segment
