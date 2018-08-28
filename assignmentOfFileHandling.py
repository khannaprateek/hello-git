#q1

f=open('Text.txt')
n=int(input("Enter the no of lines you want to read"))
for i in range(0,n+1):
       print(f.readline(),end='')
f.close()

#q2
count=0
f=open('Text.txt')
for line in f:
       count+=line.count('This')
print(count)
f.close()

#q3

with open('Text.txt' ,'r') as f:
       with open('Text2.txt' ,'w') as f2:
              for line in f:
                     f2.write(line)
with open('Text2.txt' ,'r') as f2:
       print(f2.read())

#q4
f1 = open("Text.txt")

g1 = open("Text2.txt")

f3=open("comb.text",'w')
for i,j in zip(f1,g1):
       f3.write(i+j)
f3=open("comb.text",'r')
print(f3.read())

#q5

li=[]
with open('unsort.txt' ,'r') as f:
       for i in f:
              i=str(int(i))
              li.append(i)
       li.sort()
with open('sort.txt' ,'w') as g:
       for j in li:
            g.write(j)

with open('sort.txt' ,'r') as g:
       print(g.read())

