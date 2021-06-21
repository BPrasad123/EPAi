# polygonsequence.py

import os
os.chdir(r'C:\Users\bhaga\Documents\EPAI\S14')

from polygon import Polygon
from functools import lru_cache

class PolySeq():
    '''
    Lazy implementation with iterator
    
    Custom sequence of polygons
    inputs : 
            num_edges - sequence of polygons with maximum num_edges
            circumradius - common circumradius for all the polygons
    properties :
           max_efficiency_polygon - returns the Polygon with the highest area: perimeter ratio
    '''
    def __init__(self, num_edges, circumradius):
        if type(num_edges) is not int:
            raise TypeError("Number of edges must be an integer")
        if num_edges < 3:
            raise ValueError("Number of edges must be >= 3")
        if type(circumradius) not in [float, int]:
            raise TypeError("Circumradius must be a number")
        self.num_edges = num_edges
        self._circumradius = circumradius
        PolySeq._circumradius = circumradius

    @property
    def num_edges(self):
        return self._num_edges

    @num_edges.setter
    def num_edges(self, num_edges):
        self._num_edges = num_edges
        self._max_efficiency = None

    def __len__(self):
        return self._num_edges - 2
    
    def __getitem__(self, s):
        if isinstance(s, int):
            if s < 0:
                s = self._num_edges - 2 + s
            if s < 0 or s >= (self._num_edges - 2):
                raise IndexError
            else:
                return PolySeq._poly(s)
        else:
            start, stop, step = s.indices(self._num_edges - 2)
            rng = range(start, stop, step)
            return [PolySeq._poly(i) for i in rng]

    @staticmethod 
    @lru_cache(2**10)
    def _poly(n):
        return Polygon(n + 3, PolySeq._circumradius)

    @property
    @lru_cache(1)
    def max_efficiency_polygon(self):
        if self._max_efficiency is None: 
            self._max_efficiency = sorted(self, key = lambda p: p.area / p.perimeter, reverse=True)[0]
        return self._max_efficiency

    def __repr__(self):
        return f"{tuple(self)}"

    def __len__(self):
        return self._num_edges - 2

    def __iter__(self):
        return self.PolySeqIterator(self.__len__(), self._circumradius)

    def __reversed__(self):
        return self.PolySeqIterator(self.__len__(), self._circumradius, reverse=True)

    class PolySeqIterator:
        def __init__(self, length, circumradius, reverse=False):
            self._index = 0
            self._length = length
            self._circumradius = circumradius
            self._reverse = reverse

        def __iter__(self):
            return self

        def __next__(self):
            if self._index >= self._length:
                raise StopIteration
            else:
                if self._reverse:
                    idx_element = self._length -1 - self._index
                else:
                    idx_element = self._index
                self._index += 1
                return PolySeq._poly(idx_element)