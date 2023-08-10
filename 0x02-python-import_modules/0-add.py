#!/usr/bin/python3
add_module = __import__('add_0')
add_function = add_module.add
a = 1
b = 2
result = add_function(a, b)
print("{} + {} = {}".format(a, b, result))
