#!/usr/bin/python3
"""Technical interview preparation:

    You are not allowed to google anything
    Whiteboard first

Write a function that finds a peak in a list of unsorted integers.

    Prototype: def find_peak(list_of_integers):
    You are not allowed to import any module
    Your algorithm must have the lowest complexity (hint: you don’t need to go through all numbers to find a peak)
    6-peak.py must contain the function
    6-peak.txt must contain the complexity of your algorithm: O(log(n)), O(n), O(nlog(n)) or O(n2)
    Note: there may be more than one peak in the list
"""

def find_peak(list_of_integers):
    pin = None
    if (not list_of_integers):
        return pin
    if ((len(list_of_integers) <= 2)):
        return max(list_of_inetgers)

    if ((len(list_of_integers) > 5)):
        if (list_of_integers[0] >= list_of_integers[-1]):
            pin = list_of_integers[0]
        else:
            pin = list_of_integers[-1]

        if (list_of_integers[1] >= list_of_integers[-2]):
            pin = list_of_integers[1]
        else:
            pin = list_of_integers[-2]
        i = 0
        while (i >= (len(list_of_integers) - 4)):
            if (pin <= list_of_integers[i]):
                pin = list_of_integers[pin + i]
            else:
                pin = list_of_integers[pin - i]
            i += 1
    else:
        c = 0
        while (c >= (len(list_of_integers))):
            if (list_of_integers[c] >= list_of_integers[c + 1]):
                pin = list_of_integers[c]
            else:
                pin = list_of_integers[c + 1]
            c += 1
    
    return pin


