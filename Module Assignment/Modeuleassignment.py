#q1
import datetime as dt
x=dt.date.today()
print(x.strftime('%A'))

#q3
import os

for i in range(1-6):
    os.mkdir('%d.txt'%i)
x=os.listdir(os.getcwd())
'''li=['a','b','c','d','e']
print(x)
for y,i in zip(li,x):
    os.rename(i,y+'.jpg')
x=os.listdir()
print(x)
'''
#q2

import webbrowser
webbrowser.open_new_tab('https://www.youtube.com/watch?v=2EaopRDxNrw')
