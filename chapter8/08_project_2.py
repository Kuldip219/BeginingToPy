def factorial(n):
    if (n == 1 or n == 0):
        return 1
    else:
        return n * factorial(n - 1)

n = int(input("Please enter a number to find its factorial: "))
print(f"The factorial of {n} is: {factorial(n)}")

# This code defines a recursive function to calculate the factorial of a number.