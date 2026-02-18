'''Ask the user for two values, store them in variables, swap them without using a third
variable, and print the result.'''


a,b = map(int,input("Enter the value of a and b : ").split())
print(f"The current value of variable a is {a}, b is {b} ")
a,b = b,a
print(f"The value of variable after swap a is {a}, b is {b} ")