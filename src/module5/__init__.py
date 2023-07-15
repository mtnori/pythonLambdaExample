# import _module05.hello() as hello05() in the same directory
from ._module05 import hello as hello05
# import module06.hello() as hello06() in the same directory
from .module06 import hello as hello06

print("in __init__.py")

__all__ = ['hello05', 'hello06']

# Do initialize something bellow
hello05("__init__.py")
hello06("__init__.py")
