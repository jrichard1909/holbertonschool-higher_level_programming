#!/usr/bin/python3
def uniq_add(my_list=[]):
    suma = 0
    for num in set(my_list):
        suma += num
    return (suma)
