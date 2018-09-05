from math import *
#q1
li=[1,2,3,4,5]
l=[i**3 for i in li]
print(l)

#q2

lis=[x for x in range(2, 20)
     if all(x % y != 0 for y in range(2, x))]
print(lis)

#q3
'''

The difference between the two kinds of expressions is that
the List comprehension is enclosed in square brackets []
while the Generator expression is enclosed in plain parentheses ().

Therefore the list comprehension returns a list
while the generator expression return a generator

We can access the elements of the list
but if we try to access the elements of the generator we get a TypeError'''

#q4

Celsius = [39.2, 36.5, 37.3, 37.8]
li=list(map(lambda x: (x*1.8)+32,Celsius))
print(li)

#q5
import sympy
num=[1,2,3,4,5,6,7,8,9]
li = list(filter(lambda x: True if sympy.isprime(x) else False, num))
print(li)

number = [1,2,3,4,5]
li=list(map(lambda x: x**2,number))
print(li)

#q7
from functools import *

li=[1,2,3,4,5]
product = reduce((lambda x, y: x * y), li)
print(product)

