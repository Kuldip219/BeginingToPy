class animals:
    pass

class pets(animals):
    pass

class cat(pets):
    def __init__(self):
        print("The cat says.... \n Meowwwwwwwww")

class dog(pets):
    def __init__(self):
        print("      and \n The dog says.... \n Woof Woof!")


a = cat()
b = dog()