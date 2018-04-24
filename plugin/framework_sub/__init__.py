# This plugin subtracts 2 values

from framework.plugin_base import PluginBase


class SubtractPlugin(object):
    def match(self, operation):
        return operation == 'subtract'

    # def operate(self, value1, value2):
    #     return value1 - value2


# This is executed on import!
PluginBase.register(SubtractPlugin)
