# cos_func.py

__all__ = ['cos']


import math

from .utils import print_f

@print_f
def cos(x):
    return math.cos(x)

@print_f
def cos_diff(x):
    return -math.sin(x)
