#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg_c = len(sys.argv)
    if arg_c == 1:
        arg_t = "arguments."
    elif arg_c == 2:
        arg_t = "argument:"
    else:
        arg_t = "arguments:"
    print("{} {}".format(arg_c - 1, arg_t))
    if arg_c > 1:
        for n in range(1, arg_c):
            print("{}: {}".format(n, sys.argv[n]))
