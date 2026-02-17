class salary:
    def __init__(self, name, salary, increment):
        self.name = name
        self.salary = salary
        self.increment = increment
    @property
    def salaryafterincrement(self):
        return (self.salary + self.salary * (self.increment / 100))
    
a = input("Enter your name: ")
b = float(input("Enter your salary: "))
c = float(input("Enter the increment: "))
m = salary(a, b, c)
print(f"{m.name} will earn {m.salaryafterincrement} dollars after the increment.")