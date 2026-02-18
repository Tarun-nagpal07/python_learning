'''Take a sentence from the user, split it into words, and use a set to find and print all unique
words sorted alphabetically.'''

s = list(input("Enter you sentence : ").split())
print(sorted(set(s)))