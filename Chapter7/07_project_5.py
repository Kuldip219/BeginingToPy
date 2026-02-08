n = int(input("Enter a number: "))

for i in range(1, n + 1):
    print(" "* (n - i), end="")
    print("*"* (2*i-1))

# This code prints a pyramid pattern of stars based on the input number.