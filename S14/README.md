# Session 14 - EPAI

### Assignment

The starting point for this project is the Polygon class and the Polygons sequence type we created in the previous project (assignment 13).

The code for these classes along with the unit tests for the Polygon class are below if you want to use those as your starting point. But use whatever you came up with in the last project.

**Objective 1: Polygon Class**
Goal:
Refactor the Polygon class so that all the calculated properties are lazy properties, i.e. they should still be calculated properties, but they should not have to get recalculated more than once (since we made our Polygon class "immutable").

1. Create a Polygon Class:
   1. where initializer takes in:
      1. number of edges/vertices
      2. circumradius
   2. that can provide these properties:
      1. number of edges
      2. number of vertices
      3. interior angle
      4. edge length
      5. apothem
      6. area
      7. perimeter
   3. that has these functionalities:
      1. proper `__repr__` function
      2. implements equality (==) based on number of vertices and circumradius (`__eq__`)
      3. implements > based on number of vertices only (`__gt__`)
      4. initialized to None while setting values for edge and actually calculated when called  

**Objective 2: Custom sequence of polygons**
Goal:
Refactor the Polygons (sequence) type, into an iterable. Make sure also that the elements in the iterator are computed lazily - i.e. you can no longer use a list as an underlying storage mechanism for your polygons.

You'll need to implement both an iterable, and an iterator.
1. Implement a Custom Polygon sequence type:
   1. where initializer takes in:
      1. number of vertices for largest polygon in the sequence
      2. common circumradius for all polygons
   2. that can provide these properties:
      1. max efficiency polygon: returns the Polygon with the highest **area: perimeter** ratio
      2. initialized to None while setting values for edge. Those are actually calculated when called.
   3. that has these functionalities:
      1. functions as a sequence type (`__getitem__`)
      2. supports the len() function (`__len__`)
      3. has a proper representation (`__repr__`)
      4. has a proper representation (`__iter__`)
      5. has a proper representation (`__next__`)
      6. an iterator class inside the iterable