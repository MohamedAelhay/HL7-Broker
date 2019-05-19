from abc import ABCMeta, abstractmethod


class IField:
    __metaclass__ = ABCMeta
    @abstractmethod
    def create_field(self, field):
        pass
