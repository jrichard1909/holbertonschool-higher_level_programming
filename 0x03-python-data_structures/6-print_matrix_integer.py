#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        for y in x:
            if y is not x[len(x) - 1]:
                print("{:d}".format(y), end=" ")
            else:
                print("{:d}".format(y), end="")
        print()
