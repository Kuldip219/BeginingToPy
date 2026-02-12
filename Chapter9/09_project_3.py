f = open("Chapter9/09_project_1.txt")

line = f.readline()
while line != "":
    print(line)
    line = f.readline()

f.close()