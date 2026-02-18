a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

if (a == 0) or (b == 0):
    raise ZeroDivisionError("Cannot divided by zero")
else:
    print(f"{a} divided by {b} is {a/b}")