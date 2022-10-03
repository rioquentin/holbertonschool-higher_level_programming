#!/usr/bin/python3
def roman_to_int(roman_string):
    if isinstance(roman_string, str) is False or roman_string == None:
        return 0
    number = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result = 0
    prev = 0
    for i in roman_string:
        for x in number:
            if i == x:
                actual = number.get(x)
                if result != 0:
                    if actual > prev:
                        result -= number.get(x)
                    else:
                        result += number.get(x)
                    prev = number.get(x)
                else:
                    result = number.get(x)
                    prev = number.get(x)
    return result
