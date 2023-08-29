#!/usr/bin/python3

def magic_calculation(a, b):
    result = 0
    for j in range(1, 3):
        try:
            if j > a:
                raise Expectation('Too far')
            result = result + a ** b / j
        except:
            result = b + a
            break
    return result
