class employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"{self.name} earns {self.salary} dollars."
    
a = input("Enter your name: ")
b = input("Enter your salary: ")
m = employee(a, b)
print(m)