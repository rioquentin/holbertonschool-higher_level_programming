#!/usr/bin/python3

def matrix_divided(matrix, div):
    for row in matrix:
        for column in row:
            if type(column) is not int:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    size_0 = len(matrix[0])
    b = 0
    turn = 0
    for a in matrix:
        if len(a) == size_0:
            b += 1
        turn += 1
    if b != turn:
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    newMatrix = []
    tmp = []

    for i in range(0, len(matrix)):
        for x in range(0, len(matrix[0])):
            current = float("{:.2f}".format(matrix[i][x]))
            result = float("{:.2f}".format(current / div))
            tmp.append(result)
        newMatrix.append(tmp.copy())
        tmp.clear()
    return newMatrix
