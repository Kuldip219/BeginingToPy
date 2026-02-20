from functools import reduce
l = [1, 55, 67, 23, 89, 34, 12, 90]

def greater_than_70(n):
    if n > 70:
        return True
    else:
        return False

m = list(filter(greater_than_70, l))
print(m)
    