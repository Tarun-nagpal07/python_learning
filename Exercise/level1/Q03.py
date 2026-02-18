'''Take two numbers from the user and print the result of all six operations: addition,
subtraction, multiplication, division, floor division, and modulo.'''

a,b = map(int, input("Enter two numbers : ").split())

print("Addtion : " , a+b)
print("subtraction : " , a-b)
print("multiplication : " , a*b)
print("division : " , a/b)
print("floor division : " , a//b)
print("modulo : " , a%b)