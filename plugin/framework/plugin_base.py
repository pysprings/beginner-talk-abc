from abc import ABCMeta, abstractmethod


class PluginBase(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def match(self, value):
        pass

    @abstractmethod
    def operate(self, value1, value2):
        pass
