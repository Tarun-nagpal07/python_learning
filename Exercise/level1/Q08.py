'''Take a numeric score (0-100) and print the corresponding letter grade: A (90+), B (80+), C
(70+), D (60+), F (below 60).'''


mark = int(input("Enter the marks : "))
grade = ''
if 100 >= mark >90:
    grade = 'A'
elif mark >80:
    grade = 'B'
elif mark >70:
    grade = 'C'
elif mark >60:
    grade = 'D'
elif mark >= 0:
    grade = 'F'
else:
    print("Invalid input.")
    exit()

print('Grade : ', grade)