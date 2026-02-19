mylist = [1, 5, 3, 10, 7, 4]

for index, item in enumerate(mylist):
    print(f"The item at index {index} is {item}")


squaredlist = [item ** 2 for item in mylist]
print(squaredlist)