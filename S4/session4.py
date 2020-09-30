import random
from decimal import Decimal
import cmath

class Qualean:

    permitted_inputs = [1, 0, -1, 1.0, 0.0, -1.0]

    def __init__(self, inp_nbr = 0):
        if inp_nbr not in self.permitted_inputs:
            raise ValueError("Input value must be 1 or 0 or -1")
        self.nbr = Decimal(str(inp_nbr * round(random.uniform(-1, 1), 10)))

    def __and__(self, other):
        return bool(other) and self.nbr

    def __or__(self, other):
        return bool(other) or self.nbr

    def __repr__(self):
        return str(self.nbr)

    def __str__(self):
        return str(self.nbr)

    def __add__(self, other):
        if isinstance(other, Qualean):
            return self.nbr + other.nbr
        if type(other) != str:
            return self.nbr + other
        else:
            raise ValueError('Number cannot be added with string')

    def __eq__(self, other):
        if isinstance(other, Qualean):
            return self.nbr == other.nbr
        else:
            return False

    def __float__(self):
        return float(self.nbr)

    def __ge__(self, other):
        if isinstance(other, Qualean):
            return self.nbr >= other.nbr
        elif type(other) != str:
            return self.nbr >= other
        else:
            raise ValueError('Number cannot be compared with string')

    def __gt__(self, other):
        if isinstance(other, Qualean):
            return self.nbr > other.nbr
        elif type(other) != str:
            return self.nbr > other
        else:
            raise ValueError('Number cannot be compared with string')
    def __invertsign__(self):
        return self.nbr * (-1)

    def __le__(self, other):
        if isinstance(other, Qualean):
            return self.nbr <= other.nbr
        elif type(other) != str:
            return self.nbr <= other
        else:
            raise ValueError('Number cannot be compared with string')

    def __lt__(self, other):
        if isinstance(other, Qualean):
            return self.nbr < other.nbr
        elif type(other) != str:
            return self.nbr < other
        else:
            raise ValueError('Number cannot be compared with string')

    def __mul__(self, other):
        if isinstance(other, Qualean):
            return self.nbr * other.nbr
        else:
            return self.nbr * other

    def __sqrt__(self):
        if self.nbr < 0:
            return cmath.sqrt(self.nbr)
        else:
            return self.nbr.sqrt()

    def __bool__(self):
        return bool(self.nbr)
