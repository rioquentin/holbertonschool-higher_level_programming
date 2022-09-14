#!/usr/bin/python3
def tuple_formater(a=()):
    new = tuple()
    if len(a) < 2:
        if len(a) == 1:
            new = (a[0], 0)
        elif len(a) == 0:
            new = (0, 0)
        return new
    elif len(a) > 2:
        new = a[0:2]
        return new
    else:
        return a

def add_tuple(tuple_a=(), tuple_b=()):
    a = tuple_formater(tuple_a)
    b = tuple_formater(tuple_b)
    return(tuple(p+q for p, q in zip(a, b)))
