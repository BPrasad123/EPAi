# tanh_func.py

__all__ = ['tanh']

import math

from .utils import print_f

@print_f
def tanh(x):
    return math.tanh(x)

@print_f
def tanh_diff(x):
    return 1 - (tanh(x) ** 2)
