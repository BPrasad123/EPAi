# polygon.py

import math

class Polygon():
    '''
    Polygon class
    inputs : 
            edges - number of edges/vertices
            circumradius - circumradius of the circle
    properties :
            nbr_edges - number of edges
            nbr_vertices - number of vertices
            circumradius - circumradius of the circle
            interior_angle - interior angle
            edge_length - edge length
            apothem
            area
            perimeter
    '''
    def __init__(self, edges, circumradius):
        if type(edges) is not int:
            raise TypeError("Number of edges must be an integer")
        if edges < 3:
            raise ValueError("Number of edges must be >= 3")
        if type(circumradius) not in [float, int]:
            raise TypeError("Circumradius must be a number")
        self._edges = edges
        self._circumradius = circumradius
    
    @property
    def nbr_edges(self):
        return self._edges

    @property
    def nbr_vertices(self):
        return self._edges
    
    @property
    def circumradius(self):
        return self._circumradius
    
    @property
    def interior_angle(self):
        return (self.nbr_edges - 2) * (180 / self.nbr_edges)
    
    @property
    def edge_length(self):
        return 2 * self.circumradius * math.sin(math.pi / self.nbr_edges)
    
    @property
    def apothem(self):
        return self.circumradius * math.cos(math.pi/self.nbr_edges)
    
    @property
    def area(self):
        return 0.5 * self.nbr_edges * self.apothem
    
    @property
    def perimeter(self):
        return self.nbr_edges * self.edge_length
    
    def __repr__(self):
        return f"Polygon with \n{self.nbr_edges} edges, \
                \n{self.circumradius} circumradius, \
                \n{self.interior_angle} interior angle, \
                \n{self.edge_length} edge length, \
                \n{self.apothem} apothem, \
                \n{self.area} area, \
                \n{self.perimeter} perimeter"
    
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.nbr_edges == other.nbr_edges) and (self.circumradius == other.circumradius)
        else:
            raise TypeError("Expected an instance of Polygon Class")

    def __gt__(self, other):
        if isinstance(other, self.__class__):
            return self.nbr_vertices > other.nbr_vertices
        else:
            raise TypeError("Expected an instance of Polygon Class")
