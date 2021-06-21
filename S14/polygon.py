# polygon.py

import math

class Polygon():
    '''
    Lazy implementation - property being created when explicitly called!
    
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
        self.edges = edges
        self.circumradius = circumradius
    
    @property
    def edges(self):
        return self._edges
    
    @edges.setter
    def edges(self, edges):
        self._edges = edges
        self._interior_angle = None
        self._edge_length = None
        self._apothem = None
        self._area = None
        self._perimeter = None

    @property
    def nbr_vertices(self):
        return self._edges
    
    @property
    def circumradius(self):
        return self._circumradius

    @circumradius.setter
    def circumradius(self, circumradius):
        self._circumradius = circumradius
    
    @property
    def interior_angle(self):
        if self._interior_angle is None:
            self._interior_angle = (self._edges - 2) * (180 / self._edges)
        return self._interior_angle
    
    @property
    def edge_length(self):
        if self._edge_length is None:
            self._edge_length = 2 * self._circumradius * math.sin(math.pi / self._edges)
        return self._edge_length
    
    @property
    def apothem(self):
        if self._apothem is None:
            self._apothem = self._circumradius * math.cos(math.pi/self._edges)
        return self._apothem
    
    @property
    def area(self):
        if self._area is None:
            self._area = 0.5 * self._edges * self.apothem
        return self._area
    
    @property
    def perimeter(self):
        if self._perimeter is None:
            self._perimeter = self._edges * self._edges
        return self._perimeter
    
    def __repr__(self):
        return f"Polygon with \n{self._edges} edges, \
                \n{self.circumradius} circumradius, \
                \n{self.interior_angle} interior angle, \
                \n{self.edge_length} edge length, \
                \n{self.apothem} apothem, \
                \n{self.area} area, \
                \n{self.perimeter} perimeter"
    
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self._edges == other._edges) and (self._circumradius == other._circumradius)
        else:
            raise TypeError("Expected an instance of Polygon Class")

    def __gt__(self, other):
        if isinstance(other, self.__class__):
            return self.nbr_vertices > other.nbr_vertices
        else:
            raise TypeError("Expected an instance of Polygon Class")
