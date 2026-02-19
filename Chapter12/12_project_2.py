mylist = [1, 5, 3, 10, 7, 4]

# The code below will print the items in the list along with their index.

for index, item in enumerate(mylist):
    print(f"The item at index {index} is {item}")

print("\nHere is the list with squared numbers....")

# The code below will create a new list that contains the squares of the items in the original list.

squaredlist = [item ** 2 for item in mylist]
print(squaredlist)