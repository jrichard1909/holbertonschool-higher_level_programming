#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or isinstance(roman_string, str) is False:
        return (0)
    else:
        num = 0
        len_s = len(roman_string)
        roman_ints = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                      'C': 100, 'D': 500, 'M': 1000}
        if len(roman_string) == 1:
            num = roman_ints.get(roman_string)
        else:
            for i in range(len_s):
                rom = roman_ints.get(roman_string[i])
                if i < len_s-1 and rom < roman_ints.get(roman_string[i+1]):
                    num -= rom
                else:
                    num += rom
        return (num)
