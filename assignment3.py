#q1
print("Question 1")
list_=[]
size=int(input("Enter the size of the list"))
while(size):
    a=int(input("Enter the elemnt to add to the list"))
    list_.append(a)
    size-=1
print(list_)



#q2
print("Question 2")
list2=["google","apple","facebook","microsoft","tesla"] 
list_=list_+list2
print(list_)

#q3
print("Question 3")
list_=[]
size=int(input("Enter the size of the list"))
size_=size
while(size):
    a=int(input("Enter the elemnt to add to the list"))
    list_.append(a)
    size-=1
while(size_):
    count=list_.count(list_[size_ -1])
    print("%d occurs %d times in list"%(list_[size_-1],count))
    size_-=1
    


#q4
print("Question 4")
numbers=[]
size=int(input("Enter the size of the list"))
while(size):
    a=int(input("Enter the elemnt to add to the list"))
    numbers.append(a)
    size-=1
numbers.sort()
print(numbers)



#q5
print("Question 5&6")
A=[1,3,5,7,9]
B=[2,4,6,8,10]
C=[]
C=A+B
C.sort()
print(C)



#q6 in continuation with q5

CountOdd=0
CountEven=0
for i in C:
    if(i%2 is 0):
        CountEven+=1
    else:
        CountOdd+=1
print("There are %d odd elements in the list"%(CountOdd))
print("There are %d even elements in the list"%(CountEven))

#q7print("Question 1")
print("Question 7")
tup=('This','is','a','tuple')
length=len(tup)-1
while(length>=0):
    print(tup[length],end=" ")
    length-=1
print()
#q8
print("Question 8")
tup=(1,2,5,4,3)
print('''Maximum element in the tuple is "{}" and minimum is "{}"'''.format(max(tup),min(tup)))

#q9
print("Question 9")
s="hello world"
s=s.upper()
print(s)


#q10
print("Question 10")
s="12345689"
if(s.isnumeric()):
    print("TRUE")
else:
    print("FALSE")

#q11
print("Question 11")
s="Hello World"
s=s.replace("World","Prateek")
print(s)

