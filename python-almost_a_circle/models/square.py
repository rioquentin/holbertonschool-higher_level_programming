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
