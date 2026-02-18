'''Take a paragraph of text and build a dictionary mapping each unique word to how often it
appears. Print the 5 most frequent words.'''
from collections import Counter

para = input("Enter paragraph : ")

d = {}

for p in para.lower().split():
    d[p] = d.get(p,0)+1

# print(d)
freq = Counter(d)

top = freq.most_common(5)

for w,c in top:
    print(w + ":" + str(c))