#q1

list_=['this ', 'is','a','list']
list_.reverse()
print(list_)

#q2

string_="This is A String"
for i in string_:
    if i.isupper():
        print(i,end=" ")

#q3
i=input()
list_=[]
list_=i.split(",")
list_=[int(j) for j in list_]
print(list_)

#q4
str=input()
l=int(len(str)/2)
j=-1
for i in range(0,l) :
    if str[i] is str[j]:
        flag=0
    else:
        flag=1
    j-=1
if flag is 0:
    print("String is pallindrome")
else:
    print("String is not a pallindrome")


#q5
import copy as c
#deep copy
list1 = [1, 2, [3,5], 4]
list2 = c.deepcopy(list1)
print ("Before deep copying")
print(list1)
list2[2][1] = 125
print ("After deep copying in list2")
print(list2)
print ("After deep copying in list1")
print(list1)
print('\r')
#shallow copy
list1 = [1, 2, [3,5], 4]
list2 = c.copy(list1)
print ("Before shallow copying")
print(list1)
list2[2][1] = 125
print ("After shallow copying in list2")
print(list2)
print ("After shallow copying in list1")
print(list1)

print("From above program we can conclude that shallow copy doesn't make another copy of that object")
print("But in case of Deep copy another object is created")

