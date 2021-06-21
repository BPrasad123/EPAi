# log_func.py

__all__ = ['log']

import math

from .utils import print_f

@print_f
def log(x):
    return math.log(x)

@print_f
def log_diff(x):
    return 1 / x
