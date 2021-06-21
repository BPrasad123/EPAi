# polygonsequence.py

# import os
# os.chdir(r'C:\Users\###################################')

from polygon import Polygon
from functools import lru_cache

class PolySeq():
    '''
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
        self._num_edges = num_edges
        self._circumradius = circumradius
        PolySeq._circumradius = circumradius
    
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
        return sorted(self, key = lambda p: p.area / p.perimeter, reverse=True)[0]

    def __repr__(self):
        return f"{tuple(self)}"