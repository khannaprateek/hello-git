#q1
a=3
try:
     if a<4:
      a=a/(a-3)
except ZeroDivisionError:
    print("Zero division error")
    print(a)
#q2
li=[1,2,3]
try:
     print(li[3])
except IndexError:
     print("Index Error: Index out of range\n")
     print (li)
#q3

#OUTPUT = An Exception
#        NameError: Hi there

#q4

#-5.0
#a/b result in 0

#q5
try:
     a=int(input())
     print(a)
except ValueError:
     print("Enter desired input")

lis=[1,2,3]
try:
  print(lis[3])
except IndexError:
  ("Index Error: Index out of range\n")
  print (lis)
try:
    import xyz
except ImportError as msg:
    print(msg)
