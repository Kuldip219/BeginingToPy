class calculator:
    def __init__(self, num):
        self.num = num

    def square(self):
        print(f"The square of {self.num} is {self.num ** 2}")

a = calculator(int(input("Enter a number: ")))
a.square()
