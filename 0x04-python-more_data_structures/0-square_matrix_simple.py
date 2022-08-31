#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []
    for i in matrix:
        new = new.append(sqr(lambda i: i ** 2))
    return new
