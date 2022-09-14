#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix:
        new = list(map(list, matrix))
        for x in new:
            for i in range(len(x)):
                x[i] = x[i] ** 2
        return new
    else:
        return matrix
