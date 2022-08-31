#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    def power_2(num):
        nsum = num ** 2
        return nsum
    alist = []
    if matrix[i] != '\0':
        alist.append(power_2(i))
        i += 1
        square_matrix_simple
    return alist
