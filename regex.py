import re

emails=''' abc@gmail.com
            xyz@yahoo.com
            xyz.yahoo.com
            str892@gmail.@com
            Psan.dj_a@hotmail.com'''
pattern= re.compile('[a-zA-Z0-9_.]+@{1}[a-zA-Z0-9]+\.[a-zA-Z0-9]+')
matches= pattern.findall(emails)
for i in matches:
    print(i)


#q2

print("ques2")
numbers=''' +91123456789 +8 23658974 +91987654321 +918652398745 +916230525302 '''
pattern = re.compile(r'[+]91[6-9][0-9]{9}')
matches = pattern.findall(numbers)
for i in matches:
    print(i)
    
