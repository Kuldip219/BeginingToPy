from functools import reduce

# This is a simple example of using a lambda function and map function.


l = [1, 2, 3, 4, 5, 6]

cube = lambda x: x ** 3

cubed_l = list(map(cube, l))
print(cubed_l)

# This is a simple example of using a filter function.

def even(n):
    if n % 2 == 0:
        return True
    else:
        return False

even_numbers = list(filter(even, l))
print(even_numbers)

# This is a simple example of using a reduce function.

def sum(a, b):
    return a + b

print(reduce(sum, l))