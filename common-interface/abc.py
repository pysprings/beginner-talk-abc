'''
This script demonstrates the use of ABC to enforce an interface.  Anyone who
uses a subclass is guaranteed that a method exists on that object.
'''
from abc import ABCMeta, abstractmethod


class MyABC(object):
    __metaclass__ = ABCMeta

    @abstractmethod  # <-- means subclasses *MUST* override this
    def display(self):
        print "%r : display in MyABC" % self


# This will raise TypeError
# t = MyABC()

class MyClass(MyABC):
    def display(self):
        print "%r : display in MyClass" % self

        # You can use super() to call the ABC method where appropriate
        super(MyClass, self).display()


class MySecondClass(MyABC):
    def display(self):
        print "%r : display in MySecondClass" % self


b = MyClass()
c = MySecondClass()

b.display()
c.display()
