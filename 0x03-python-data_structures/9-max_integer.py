#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list):
        b = 0
        c = 0
        for a in my_list:
            b = (a if a > b else b)
        return (b)
    else:
        return (None)
