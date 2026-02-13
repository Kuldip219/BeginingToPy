words = ["racism", "bad"]

with open("File_Io/09_project_6.txt", "r") as file:
    content = file.read()
for word in words:
    content = content.replace(word, "*" * len(word))

with open("File_Io/09_project_6.txt", "w") as file:
    file.write(content)

# End of the code.