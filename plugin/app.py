'''
Mock up of a plugin-based application that uses `ABC.register()`.  Each plugin
is expected to have both `match()` and `operate()` methods.

This simulates an enviroment where you have plugins to perform different
operations on data (e.g. add, subtract, etc).
'''
from framework.plugin_base import PluginBase
from framework_add import AddPlugin   # noqa: F401
from framework_mult import MultiplyPlugin   # noqa: F401
from framework_sub import SubtractPlugin   # noqa: F401


def get_plugin_object(plugins, operation):
    '''
    Search through all plugins looking for a match.

    :returns: The class that matches the operation
    '''
    for plugin in plugins:
        if plugin.match(operation):
            return plugin

    raise StopIteration('operation not found: %s' % operation)


if __name__ == '__main__':
    # Initialize all of the plugins
    # Notice that I haven't directly created object types.  They are kept in
    # `_abc_registry`.
    plugins = [x() for x in PluginBase._abc_registry]
    print "all of my plugins:", plugins
    print

    print "example operations:"
    print "    add 2 3"
    print "    multiply 2 3"

    user_input = raw_input('Enter the operation to perform: ')
    while user_input:
        operation, value1, value2 = user_input.split()
        value1 = int(value1)
        value2 = int(value2)
        plugin = get_plugin_object(plugins, operation)
        print "%r : plugin.operate(%i, %i) = %s" % (plugin, value1, value2, plugin.operate(value1, value2))

        user_input = raw_input('Enter the operation to perform: ')

    # This will raise an `AttributeError` because SubtractPlugin doesn't have
    # an `operate()` method.
    # operation = 'subtract'
    # plugin = get_plugin_object(plugins, operation)
    # print "%r : plugin.operate(2, 4) = %s" % (plugin, plugin.operate(2, 4))
