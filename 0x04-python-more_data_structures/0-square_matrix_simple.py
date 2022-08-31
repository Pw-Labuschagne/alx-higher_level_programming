#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    def power_2(num):
        pwr = num ** 2
        return pwr
    return power_2


for i in range(matrix):
    power_func = square_matrix_simple(i)

print(power_func)
