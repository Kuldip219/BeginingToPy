n = int(input("Enter a number: "))

for i in range(2, n):
    if n % i == 0:
        print("Number is not prime")
        break
else:
    print("Number is prime")

# This code checks if a number is prime or not using a for loop.