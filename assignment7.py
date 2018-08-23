#q1
dict={}
list_=[]
i=int(input("Enter the no of elements you want to enter"))
while(i):
    n=int(input())
    dict[n]=input()
    i-=1
for i in dict.values():
    print(i)


#q2

Students={'student1':{'maths':35,'ds':50},'student2':{'maths':46,'ds':40}}
Students['student3']={'maths':45,'ds':50}
print("Marks of student3 are:",Students['student3'])
