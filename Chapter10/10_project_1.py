class student():
    age = 20   
    subject = "Math"
    grade = "A+"

a = student()
name = input("Enter name: ")
a.name = name
print(a.name, a.age, a.subject, a.grade)