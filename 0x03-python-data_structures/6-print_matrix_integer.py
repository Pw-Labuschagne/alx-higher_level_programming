#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    def print_matrix_integer(matrix=[[]]):
    for z in range(len(matrix)):
        for i in range(len(matrix[z])):
            if i != 0:
                print(" ", end='')
            print("{:d}".format(matrix[z][i]), end='')
        print()
