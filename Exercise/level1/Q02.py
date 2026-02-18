'''Prompt the user to enter five different values. Print each value along with its Python data
type using type().'''

import re

ls = list(input("Enter five types of different values : ").split())

for i in ls:
    try:
        # if re.match('[a-zA-z]+',i):
        #     print(f"{i} is type of {type(i).__name__}")
        # else :
            value = eval(i)
            print(f"{value} is type of {type(value).__name__}")

    except ValueError as e:
        print(f"{i} is of type {type(i)}")



