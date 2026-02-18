'''Generate a list of 50 random integers between 1 and 100. Find and print the minimum,
maximum, mean, and count of numbers that are above 75.'''

import random

ls = [ random.randint(1,100) for _ in range(50) ]


print("Minimum :", min(ls))
print("Maximum :", max(ls))
print('Mean : ', sum(ls)/len(ls))
count = [i for i in ls if i>75] 
print("More than 75 :", len(count))
# print(ls)