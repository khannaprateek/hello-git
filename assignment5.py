#q1

year=int(input())
if year%4==0:
    if year%100 ==0:
        if year%400 is 0:
            print("{} is a leap year".format(year))
        else:
            print("{} is not a leap year".format(year))
    else:
       print("{} is not a leap year".format(year))
else:
    print("{} is not a leap year".format(year))


#q2
length=int(input("Enter the value of length"))
breadth=int(input("Enter the value of breadth"))
if length is breadth:
    print("It is a square")
else:
    print("It is a rectangle")

#q3
A=int(input("Enter the age"))
B=int(input("Enter the age"))
C=int(input("Enter the age"))
if A>B and A>C:
    print("A is oldest")
elif B>A and B>C:
    print("B is oldest")
elif C>A and C>B:
    print("C is oldest")
elif A is B and B is C:
    print("All are of same age")
elif A is B or A is C or B is C :
    print("More than one person have same ")

#q4

age=int(input("Enter the age"))
sex=input("Enter your sex(M or F)")
marital_status=input("Enter your marital status ( Y or N )")
if ( sex is 'f' or sex is 'F' ):
    print("You will work only in urban area")
elif 20<=age<=40:
    print("You can work anywhere")
elif 40<=age<=60:
    print("You will work only in urban area")
else:
    print("Error")


#q5
quantity=int(input("Enter the quantity"))

if quantity >1000:
    cost=quantity*100 - quantity/10
else:
    cost= quantity*100
print(cost)


#q6
s=10
while(s):
    a=int(input())
    print(a)
    s-=1

#q7
s=1
while(s):
    print(s)


#q8
list_=[]
list1=[]
size=int(input("Enter the size of the list"))
size_=size
while(size):
    a=int(input("Enter the elemnt to add to the list"))
    list_.append(a)
    size-=1
for i in list_:
    list1.append(i**2)
print(list1)


#q9
list_=[1,'a',1.2,'abc',3,3.4]
listint=[]
liststr=[]
listflo=[]
for i in list_:
    if type(i) is int:
        listint.append(i)
    elif type(i) is str:
        liststr.append(i)
    elif type(i) is float:
        listflo.append(i)
print("Int list is :",listint)
print("String list is :",liststr)
print("Float list is :",listflo)

#q10
import math as m
list_=[]
for a in range(1,101):
    if(a>1):
        k=0
        for i in range(2,a//2+1):
            if(a%i==0):
                k=k+1
        if(k<=0):
            list_.append(a)
print(list_)

#q11
for i in range(0,5):
    for j in range(0,i):
        print('*',end="")
    print()
                   
    
#q12


list_=[]
size=int(input("Enter the size of the list"))
size_=size
for i in range(0,size):
    a=int(input("Enter the elemnt to add to the list"))
    list_.append(a)
    size-=1
i=int(input())
a=list_.index(i)
if a is not 0:
    list_.remove(i)
print(list_)

    




    
    
