'''Use collections.Counter to find the 3 most common characters in a string. Use
collections.defaultdict to group a list of words by their first letter.'''

from collections import Counter,defaultdict

txt = list(input("Enter your text : ").split())

print(Counter(txt).most_common(3))

d = defaultdict(list)
for w in txt:
    d[w[0]].append(w)

print(d)
    