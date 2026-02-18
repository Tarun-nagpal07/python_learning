'''Simulate rolling two six-sided dice 100 times. Count and print how many times the combined
total equals 7.'''

import random

count = 0
for _ in range(100):
    first = random.randint(1,6)
    second = random.randint(1,6)
    count = count + 1 if first + second == 7 else count


print(f"Sum of 7 appeared {count} times out of 100 rolls.")
    