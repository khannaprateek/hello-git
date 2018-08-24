#q1

import math as m
class circle:
    def __init__(self,radius):
        self.radius=radius
    def getArea(self):
        self.area=m.pi*(self.radius**2)
        return self.area
    def getCircumference(self):
        self.circumference =2 *m.pi * self.radius
        return self.circumference
c=circle(5)
print(c.getArea())
print(c.getCircumference())

#q2

class Student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollNo=rollno
    def display(self):
        print("Name:",self.name)
        print("RollNo:",self.rollNo)
        print("Age:",self.age)
        print("Marks:",self.marks)
    def setAge(self,age):
        self.age=age
    def setMarks(self,marks):
        self.marks=marks
s=Student('Student1','1637')
s.setAge(20)
s.setMarks(500)
s.display()

#q3

class Temperature:
    def convertFahrenheit(self,celsius):
        self.temp=celsius*1.8 + 32
        return self.temp
    def convertCelsius(self,fahrenheit):
        self.temp= (fahrenheit -32)*5 /9
        return self.temp
t=Temperature()
fahrenheit,celsius=0,0
te=t.convertFahrenheit(35)
print(te)
te=t.convertCelsius(102)
print(te)
     
#q4

class MovieDetails:
    def add(self,artistname,yearofrelease,ratings):
        self.artistName=artistname
        self.yearOfRelease=yearofrelease
        self.ratings=ratings
    def display(self):
        print("ArtistName is:",self.artistName)
        print("Year of Release is:",self.yearOfRelease)
        print("Rating is:",self.ratings)
m=MovieDetails()
m.add("Jason Statham",2000,9.2)
m.display()

#q5

class Animals:
    def animal_attribute(self):
        print("This is a base class function")
class Tiger(Animals):
    pass

t=Tiger()
t.animal_attribute()

#q6

'''
It will show an Error in python version3 as there is no brackets in print statement
If brackets were there it will display following output:
A B
A B
'''

#q7

class Shape:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
        self.ar=0
    def area(self):
        self.ar=self.length * self.breadth
        return self.ar
    pass
class Rectangle(Shape):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    pass
class Square(Shape):
    def __init__(self,length):
        self.length=length
        self.breadth=length
    pass
s=Square(5)
r=Rectangle(5,6)
print(s.area())
print(r.area())
