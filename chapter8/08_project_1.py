def prog(ending):
    print("Hello! Welcome to the program.")
    name = input("Please enter your name: ")
    a = int(input("Please enter a number: "))
    b = int(input("Please enter another number: "))
    c = int(input("Please enter a third number: "))
    average = (a + b + c) / 3
    print("The average of the three numbers is:", average)
    print(f"Thank you for using the program, {name} \n {ending}")

prog("Have a nice day!")