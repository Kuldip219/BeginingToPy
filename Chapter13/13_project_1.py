# This is a simple example of using a lambda function and map function.

l = [1, 2, 3, 4, 5]

cube = lambda x: x ** 3

cubed_l = list(map(cube, l))
print(cubed_l)



