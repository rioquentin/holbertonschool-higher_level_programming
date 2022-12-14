#!/usr/bin/python3
''' New module for a new class'''


from models.rectangle import Rectangle


class Square(Rectangle):
    '''Class that define a square'''

    def __init__(self, size, x=0, y=0, id=None):
        ''' Constructor for square class'''

        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''overwrite str to change output of print'''

        return ("[Square] ({}) {}/{} - {}".format
                (self.id, self.x, self.y, self.width))

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        '''method to update instance attribute'''

        arg = ["id", "size", "x", "y"]
        z = 0
        if args:
            for i in args:
                setattr(self, arg[z], i)
                z += 1
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        ''' return dictonary repr of all attributes'''

        return {'id': self.id, 'x': self.x, 'size': self.size, 'y':self.y}
