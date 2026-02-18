'''Create a class EvenIterator that acts as an iterator, yielding the first N even numbers when
used in a for loop.'''


class EvenIterator:
    def __init__(self,n):
        self.n = n
        self.number = 0
        self.counter = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.counter == self.n:
            raise StopIteration
        x = self.number
        self.number += 2
        self.counter += 1
        return x
    
# for n in EvenIterator(10):
#     print(n)

n = EvenIterator(10)

print(next(n))
print(next(n))
print(next(n))
print(next(n))
        