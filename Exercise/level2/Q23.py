'''Ask the user to enter 5 students (name + grade). Write them to a text file, one per line. Then
read the file back and display the records in a formatted table.'''


f = open('student.txt','w')
f.write("..............Student Grade...................\n")
for _ in range(5):
    name = input("Enter name : ")
    grade = input("Enter Grade  : ")
    content = f"{name:<12} {grade}\n"
    f.write(content)


f.close()

with open('student.txt','r') as f:
    for line in f.readlines():
        print(line)
 