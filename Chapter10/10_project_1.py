class student():
    name = "john"
    age = 20   
    subject = "Math"
    grade = "A+"

    def info(self):
        print(self.name, self.age, self.subject, self.grade)

a = student()
a.name = input("Enter name: ")
a.info()