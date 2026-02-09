def remove(lst, value):
    n = []
    for item in lst:
        if not(item == value):
            n.append(item.strip(value))
    return n

list = ["Brinto", "Dip", "Tirtha", "Prodip", "Sourav", "Kuldip"]
lst = [item.lower() for item in list]
name = input("Enter the name you want to remove: ")
value = name.lower()
print(remove(lst, value))

# End of the code