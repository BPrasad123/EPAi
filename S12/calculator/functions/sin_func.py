# sin_func.py

__all__ = ['sin']

import math
from .utils import print_f

@print_f
def sin(x):
    return math.sin(x)

@print_f
def sin_diff(x):
    return math.cos(x)
