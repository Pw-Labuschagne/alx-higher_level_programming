#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):

    my_list_new = []

    for num in range(list_length):
        try:
            sumAll = my_list_1[num] / my_list_2[num]
        except TypeError:
            sumAll = 0
            print("wrong type")
        except ZeroDivisionError:
            sumAll = 0
            print("division by 0")
        except IndexError:
            sumAll = 0
            print("out of range")
        finally:
            my_list_new.append(sumAll)
    return(my_list_new)
