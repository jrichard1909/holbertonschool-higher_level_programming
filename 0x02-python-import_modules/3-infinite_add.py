#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg_c = len(sys.argv)
    suma = 0
    for n in range(1, arg_c):
        suma += int(sys.argv[n])
    print(int(suma))
