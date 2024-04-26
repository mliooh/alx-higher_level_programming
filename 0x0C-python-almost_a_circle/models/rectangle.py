#!/usr/bin/python3
""" Module contains class Rectangle that inherits
from Base. """
from models.base import Base


class Rectangle(Base):
    """ Class Rectangle that inherits from Base. """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initialization. """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ width property getter. """
        return self.__width

    @width.setter
    def width(self, value):
        """ Width property setter. """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Height property getter. """
        return self.__height

    @height.setter
    def height(self, value):
        """ Height property setter. """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ x property getter """
        return self.__x

    @x.setter
    def x(self, value):
        """ x property setter. """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ y property getter. """
        return self.__y

    @y.setter
    def y(self, value):
        """ Y property setter. """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Returns the area of the rectangle. """
        return self.width * self.height

    def display(self):
        """ Prints in stdout the rect with character #. """
        res = " "
        for lines in range(self.y):
            print()

        for i in range(self.height):
            for j in range(self.width + self.x):
                if j < self.x:
                    print(res, end='')
                else:
                    print("#", end='')
            print()

    def __str__(self):
        """ Returns print of object. """
        return ('[Rectangle] ({}) {}/{} - {}/{}'
                .format(self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """ Assigns an argument to each attribute. """
        if args is not None and len(args) != 0:
            list_attr = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, list_attr[i], args[i])

        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Returns the dictionary representation of a rectangle. """
        list_attr = ['id', 'width', 'height', 'x', 'y']
        dict_res = {}

        for key in list_attr:
            dict_res[key] = getattr(self, key)

        return dict_res
