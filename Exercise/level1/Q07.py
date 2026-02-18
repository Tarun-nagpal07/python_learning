'''Use a for loop to print a right-angled triangle of asterisks with a height entered by the user.'''

n = int(input("Enter the value of n : "))

for i in range(1,n+1):
    print('*'*i)
    