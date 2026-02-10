a = int(input("CT 1: "))
b = int(input("CT 2: "))
c = int(input("CT 3: "))
#d = int(input("Midterm Marks: "))
#e = int(input("Final Marks: "))


if(a > c and b > c or a==b):
    average = (a + b) / 2
    print("The average of the two highest marks is: ", average)
elif(b > a and c > a or b==c):
    average = (b + c) / 2
    print("The average of the two highest marks is: ", average)
elif(a > b and c > b or a==c):
    average = (a + c) / 2
    print("The average of the two highest marks is: ", average)

#total = average + d + e
#
#if(total > 33):
#    print("Congratulations! You passed the course with a total score of: ", total)
#else:
#    print("Sorry, you failed the course with a total score of: ", total)