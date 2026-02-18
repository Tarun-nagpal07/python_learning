'''Ask the user for a starting number. Use a while loop to count down to 0, printing each
number on a new line. Print 'Blast off!' at the end.'''

n = int(input("Enter the number : "))

while n:
    print(n)
    n -= 1

print("Blast off !! ")