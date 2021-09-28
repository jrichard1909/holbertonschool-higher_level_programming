#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for index in range(0, list_length):
        res = 0
        try:
            res = my_list_1[index] / my_list_2[index]
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            new_list.append(res)

    return new_list
