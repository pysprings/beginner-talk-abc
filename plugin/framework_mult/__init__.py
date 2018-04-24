# This plugin adds 2 values

from framework.plugin_base import PluginBase


class MultiplyPlugin(object):
    def match(self, operation):
        return operation == 'multiply'

    def operate(self, value1, value2):
        return value1 * value2


# This is executed on import!
PluginBase.register(MultiplyPlugin)
