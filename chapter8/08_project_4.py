def remove(lst, value):
    if value in lst:
        lst.remove(value)
    

lst = ["Brinto", "Dip", "Tirtha", "Prodip", "Sourav", "Kuldip"]
value = input("Please enter the value to remove from the list: ")
remove(lst, value)
print("The updated list is:", lst)