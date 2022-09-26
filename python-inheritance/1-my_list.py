#!/usr/bin/python3
'''All func and class'''


class MyList(list):
    '''class that inherit from list'''

    def print_sorted(self):
        '''Func to sort'''

        new = self.copy()
        new.sort()

        print(new)
