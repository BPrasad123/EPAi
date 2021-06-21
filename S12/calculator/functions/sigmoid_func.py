# sigmoid_func.py

__all__ = ['sigmoid']

import math

from .utils import print_f

@print_f
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

@print_f
def sigmoid_diff(x):
    return sigmoid(x)*(1 - sigmoid(x))
