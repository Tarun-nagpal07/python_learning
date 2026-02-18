'''Create a dictionary of 5 students and their scores. Print each name, their score, and
whether they passed (>=50). Also print the class average'''

students = {
    "arya": 78,
    "Bob": 45,
    "lisa": 62,
    "doku": 50,
    "hiya": 33
}

total = 0

for name, score in students.items():
    status = "Passed" if score >= 50 else "Failed"
    print(f"Name: {name:<10}, Score: {score:<10}, Status: {status:<10}")
    total += score

average = total / len(students)
print(f"\nClass Average: {average:.2f}")
