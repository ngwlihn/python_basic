import re
t = int(input())
while t>0:
    t-=1
    s=input()
    num=re.findall(r'\d+',s)
    number=[int(i) for i in num]
    print(max(number))