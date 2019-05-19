
from abc import ABCMeta, abstractmethod


class IFillable:
    __metaclass__ = ABCMeta
    @abstractmethod
    def fill_segment(self, field_number, segment, message_preparer):
        pass
