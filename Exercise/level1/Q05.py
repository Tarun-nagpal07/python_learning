'''Ask the user for their name and age, then print a personalised greeting and tell them the
year they were born.'''

import datetime

def greeting(name,year):
    print(f"Hello {name}, the were born in {year}!!!")


name , age = input("Enter the name and age : ").split()
age = int(age)

year_of_born = datetime.date.today().year - age

greeting(name,year_of_born)