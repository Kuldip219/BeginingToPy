
sub_1 = int(input("Enter marks for Subject 1: "))
sub_2 = int(input("Enter marks for Subject 2: "))
sub_3 = int(input("Enter marks for Subject 3: "))

total_marks = sub_1 + sub_2 + sub_3
percentage = (total_marks / 300) * 100

if percentage >= 40:
    print("Congratulations! You have passed the exam.")

else:
    print("Sorry, you have failed the exam. Better luck next time!")

print("your percentage is:", percentage)
