# tan_func.py

__all__ = ['tan']

import math

from .utils import print_f

@print_f
def tan(x):
    return math.tan(x)

@print_f
def tan_diff(x):
    return 1-(tan(x)** 2)
