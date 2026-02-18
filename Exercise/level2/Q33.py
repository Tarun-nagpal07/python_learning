'''Use collections.namedtuple to define an Employee record (name, department, salary).
Create 5 employees, store in a list, and print only those earning above a given threshold.'''

from collections import namedtuple

Employee = namedtuple('Employee',['name','department','salary'])

e = [
    Employee('Employeee1','aiml',10000),
        Employee('Employeee2','aiml',20200),
            Employee('Employeee3','aiml',22000),
                Employee('Employeee4','aiml',29000),
                    Employee('Employeee5','aiml',3000)
    ]

threshold = int(input("Enter your threshold : "))


for i in e:
    if i.salary > threshold:
        print(i.name,i.department,i.salary)
    