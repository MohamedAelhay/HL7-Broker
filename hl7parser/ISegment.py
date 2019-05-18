
from abc import ABCMeta, abstractmethod


class ISegment:
    __metaclass__ = ABCMeta
    @abstractmethod
    def create_segment(self, pid_segment, segment_data_dict):
        pass
