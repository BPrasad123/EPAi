# relu_func.py

__all__ = ['relu']

import math

from .utils import print_f

@print_f
def relu(x):
    return max(0, x)

@print_f
def relu_diff(x):
    if x > 0:
        return 1
    return 0
