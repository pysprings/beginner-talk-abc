# This plugin adds 2 values

from framework.plugin_base import PluginBase


class AddPlugin(object):
    def match(self, operation):
        return operation == 'add'

    def operate(self, value1, value2):
        return value1 + value2


# This is executed on import!
PluginBase.register(AddPlugin)
