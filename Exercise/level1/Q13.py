'''Store two 2D points as tuples. Write a function that calculates and returns the Euclidean
distance between them.'''

import math

p1 = tuple(map(float , input("Enter the value of coordinates : ").split()))
p2 = tuple(map(float , input("Enter the value of coordinates : ").split()))

def EuclideanDistance(p1,p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

print(f"Euclidean Distance :  {EuclideanDistance(p1,p2):.2f}")