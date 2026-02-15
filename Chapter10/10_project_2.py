class calculator:
    def __init__(self, num):
        self.num = num

    def square(self):
        print(f"The square of {self.num} is {self.num ** 2}")

    def cube(self):
        print(f"The cube of {self.num} is {self.num ** 3}")

    def square_root(self):
        print(f"The square root of {self.num} is {self.num ** 0.5}")

a = calculator(int(input("Enter a number: ")))
a.square()
a.cube()
a.square_root()

# End of the code snippet.