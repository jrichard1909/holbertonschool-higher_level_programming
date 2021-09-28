#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    cont = 0
    index = 0
    while index < x:
        try:
            print("{:d}".format(my_list[index]), end="")
            cont += 1
            index += 1
        except (TypeError, ValueError):
            index += 1
            continue
    print("")
    return cont
