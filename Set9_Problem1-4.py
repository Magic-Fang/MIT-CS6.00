# 6.00 Problem Set 9
#
# Name:
# Collaborators:
# Time:

from string import *


class Shape(object):
    def area(self):
        raise AttributeException("Subclasses should override this method.")


class Square(Shape):
    def __init__(self, h):
        """
        h: length of side of the square
        """
        self.side = float(h)

    def area(self):
        """
        Returns area of the square
        """
        return self.side ** 2

    def __str__(self):
        return 'Square with side ' + str(self.side)

    def __eq__(self, other):
        """
        Two squares are equal if they have the same dimension.
        other: object to check for equality
        """
        return type(other) == Square and self.side == other.side


class Circle(Shape):
    def __init__(self, radius):
        """
        radius: radius of the circle
        """
        self.radius = float(radius)

    def area(self):
        """
        Returns approximate area of the circle
        """
        return 3.14159 * (self.radius ** 2)

    def __str__(self):
        return 'Circle with radius ' + str(self.radius)

    def __eq__(self, other):
        """
        Two circles are equal if they have the same radius.
        other: object to check for equality
        """
        return type(other) == Circle and self.radius == other.radius


#
# Problem 1: Create the Triangle class
#
## TO DO: Implement the `Triangle` class, which also extends `Shape`.


class Triangle(Shape):
    def __init__(self, base, hight):
        self.base = float(base)
        self.hight = float(hight)

    def area(self):
        return 0.5 * self.base * self.hight

    def __str__(self):
        return 'Triangle with base ' + str(self.base) + ' and hight ' + str(self.hight)

    def __eq__(self, other):
        return type(other) == Triangle and self.base == other.base and self.hight == other.hight


#
# Problem 2: Create the ShapeSet class
#
## TO DO: Fill in the following code skeleton according to the
##    specifications.

class ShapeSet:
    def __init__(self):
        """
        Initialize any needed variables
        """
        self.all_shapes = []
        self.all_area = []
        self.circle = []
        self.square = []
        self.triangle = []
        self.number = None

    def addShape(self, sh):
        """
        Add shape sh to the set; no two shapes in the set may be
        identical
        sh: shape to be added
        """
        # if type(sh) != Shape :
        #     raise TypeError('the input is not a shape')
        # else:
        self.all_shapes.append(sh)
        self.all_area.append(sh.area())
        if type(sh) == Circle:
            self.circle.append(sh)
        elif type(sh) == Square:
            self.square.append(sh)
        elif type(sh) == Triangle:
            self.triangle.append(sh)


    def __iter__(self):
        """
        Return an iterator that allows you to iterate over the set of
        shapes, one shape at a time
        """
        self.number = 0
        return self

    def __next__(self):
        if self.number >= len(self.all_shapes):
            raise StopIteration
        self.number += 1
        return self.all_shapes[self.number - 1]

    def __str__(self):
        """
        Return the string representation for a set, which consists of
        the string representation of each shape, categorized by type
        (circles, then squares, then triangles)
        """
        return 'Circle ' + str(self.circle) + '\nSquare' + str(self.square) + '\nTriangle' + str(self.triangle)
        # TO DO


#
# Problem 3: Find the largest shapes in a ShapeSet
#
def findLargest(shapes):
    """
    Returns a tuple containing the elements of ShapeSet with the
       largest area.
    shapes: ShapeSet
    """
    # TO DO
    Larea = shapes.all_area[0]
    ind = [0]
    result = []
    for i in range(1, len(shapes.all_shapes)):
        if Larea < shapes.all_area[i]:
            ind.clear()
            ind.append(i)
            Larea = shapes.all_area[i]
        elif Larea == shapes.all_area[i]:
            ind.append(i)
    for num in ind:
        print('\nthe largest shape is\n', shapes.all_shapes[num])
        result.append(shapes.all_shapes[num])
    return result


#
# Problem 4: Read shapes from a file into a ShapeSet
#
def readShapesFromFile(filename):
    """
    Retrieves shape information from the given file.
    Creates and returns a ShapeSet with the shapes found.
    filename: string
    """
    # TO DO
    myset = ShapeSet()
    f = open(filename)
    for line in f:
        line_a = line.strip('\n')
        line_s = line_a.split(',')
        # print(line_s)
        if line_s[0] == 'circle':
            myset.addShape(Circle(line_s[1]))
        elif line_s[0] == 'square':
            myset.addShape(Square(line_s[1]))
        elif line_s[0] == 'triangle':
            myset.addShape(Triangle(line_s[1], line_s[2]))
    return myset



def test():
    s1 = Square(2)
    c1 = Circle(1)
    t1 = Triangle(2, 2)
    t2 = Triangle(4, 2)
    set1 = ShapeSet()
    set1.addShape(s1)
    set1.addShape(c1)
    set1.addShape(t1)
    set1.addShape(t2)
    for shape in set1:
        print(shape)
    largest = findLargest(set1)
    print(type(largest[0]) == Square)

def test2():
    filename = 'shapes.txt'
    myset = readShapesFromFile(filename)
    for shape in myset.circle:
        print(shape)
    for shape in myset.square:
        print(shape)
    for shape in myset.triangle:
        print(shape)


#test()
test2()