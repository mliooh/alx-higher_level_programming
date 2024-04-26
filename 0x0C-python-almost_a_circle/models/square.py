#!/usr/bin/python3
""" Module contains class Square that inherits
from Rectangle. """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class square that inherits from Rectangle. """
    def __init__(self, size, x=0, y=0, id=None):
        """ Initialization of the square. """
        super().__init__(size, size, x, y)

    def __str__(self):
        """ Returns string representation of object. """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """ Size getter. """
        return self.width

    @size.setter
    def size(self, value):
        """ Size setter. """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Method that assigns attributes."""
        if args is not None and len(args) != 0:
            list_attrs = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                setattr(self, list_attrs[i], args[i])

        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Returns the dictionary representation of a Square. """
        list_attr = ['id', 'size', 'x', 'y']
        dict_res = {}

        for key in list_attr:
            if key == 'size':
                dict_res[key] = getattr(self, 'width')
            else:
                dict_res[key] = getattr(self, key)

        return dict_res
