print("hello one!")


temp = {1,2,3}
print(type(temp))
froze = frozenset(temp)
temp.add(4)
print(temp)

print(type(froze))


data = b"hello"
print(data)
print(type(data))


d = memoryview(data)
print(d)


name = "its_python_bitch"
print(name)
print(name[2])
# name[0]= 'I'
# print(name)

print(f"hello python {3} times")

print(3/2)
print(3//2)


l = [12,3,4,5,6,10,89,90]

def key_func(n) : 
    return n/0.100

l.sort(key = key_func)
print(l)

t = (1,2,3,4)
t2 = (5,6,7,8)
# del t[0]

(one , *two , three) = t
print(one)
print(two)
print(three)


print(t + (t2)) # tuple not have extend to add tuples


dist = {
    "name" : "mercedes",
    "year" : "2020",
    "model" : "Eclass"
}

print(dist)
dist['year'] = "2019"
print(dist)
dist.update({"year":"2020"})
print(dist)

for (k,v) in dist.items():
    print(k , ": ", v)

# dist.pop("year")
# dist.popitem()
del dist["year"]
print(dist)

dist.clear()
print(dist)

def knock(name):
    print((f"knock knock?? who's there ... {name} here"))

knock("Python")

def test(name,*hobbies, **fav):
    print(name)
    print(hobbies)
    print(fav)

test("python","complexity","multithreading", lang="high_level",opt="better than C,C++")

#decorator
def change_case(func):
    def myinner():
        return func().upper()
    return myinner

#decorated
@change_case
def myfunction():
    return "Hello World!"

print(myfunction())

#argumentated decorated function
def hello(func):
    def myinner(x):
        return func(x).upper()
    return myinner

def many_arg(func):
    def myinner(*args,**kwargs):
        return func(*args,**kwargs).lower()
    return myinner

@hello
def decorated(num):
    return "Hello " + num

print(decorated("python"))

@many_arg
def args_decorative(name1,name2,name3,age):
    return f"All of them {name1} , {name2} , {name3} have same age {age} old"

print(args_decorative("python","C","Java",age = "20"))

#argumentor decorative

def changecase(n):
    def change_case_decorative(func):
        def myinner():
            if(n == 1):
                return func().upper()
            else :
               return func().lower()
        return myinner
    return change_case_decorative
@changecase(0)
def myfunc():
    return "Hello PIP"
print(myfunc())


import functools

# multiple decoratives
def changecase(func):
  @functools.wraps(func) #help to preserve the function name
  def myinner():
    return func().upper()
  return myinner

def addgreeting(func):
  @functools.wraps(func)
  def myinner():
    return "Hello " + func() + " Have a good day!"
  return myinner

@changecase
@addgreeting
def myfunction():
  return "Tobias"

print(myfunction())
print(myfunction.__name__)

x = lambda a,b,c : a+b*c
print(x(1,2,3))


def myft(n):
    return lambda a : a * n

mydoubler = myft(10)

print(mydoubler(20))

number = [1,2,3,4]

def myfunction():
    return list(map(lambda x : x * 3,number ))

print(myfunction())

odd_numbers = list(filter(lambda x : x % 2 != 0, number))
print(odd_numbers)

sort = sorted(number,key=lambda x : -x)
print(sort)

# yeild generator

def countfunc(n):
   count = 1
   while count <=n:
       yield count
       count += 1

# for num in countfunc(5):
#     print(num)
num = countfunc(5)

print(next(num))
print(next(num))

def fibo():
  a,b = 0,1
  while True:
      yield a

      a ,b = b ,a+b


num = fibo()
for _ in range(10):
    print(next(num), end= ", ")

# Iterator

class iterOperation:
    def __iter__(self):
        self.a = 1 
        return self
    def __next__(self):
        x = self.a
        self.a += 1
        return x
    
ob = iterOperation()
myiter = iter(ob)

print(" ")
print(next(myiter))

import platform
print(platform.system())

class MyExeception(Exception):
    def __init__(self):
        super()

    def __str__(self):
        print(self.message)


try:
    raise MyExeception("Error is commming")
except:
    print("done")


# m = int(input())
# print(m)