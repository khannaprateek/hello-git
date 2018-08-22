#q1

def areaOfSphere(radius):
    area=4/3 * 3.14 * (radius**2)
    return area
area=areaOfSphere(5)
print(area)

#q2

def perfect(number):
      sum=0
      for i in range(1,number):
            if number%i is 0:
                  sum=sum+i

      if sum is number:
            return number
      else:
            return 0


for i in range(1,1001):
      n=perfect(i)
      if n is not 0:
            print(n)


#q3

n=int(input("enter a number"))
for i in range(1,11):
      print(i*n)

#q4

def power(n,m):
    if m is 1:
        return n
    else :
      a= power(n,m-1)
      return (n*a)
n=int(input("enter a number"))
m=int(input("enter a number"))
number=power(n,m)
print("n^m=",number)
