
#!/usr/bin/python3
''' Empty Class'''


class Square:
    '''Empty'''

    def __init__(self, size=0):
        '''define var'''

        if isdigit(size) is False:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    pass
