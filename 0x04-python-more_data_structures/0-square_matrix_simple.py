#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    alist = []    
    for i in matrix:
        new = list(map(lambda x: x*x, i))
        alist.append(new)
        print(alist)
