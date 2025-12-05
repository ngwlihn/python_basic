import re
t = int(input())
while t>0:
    s=input()
    num=re.findall(r'\d+',s)
    number=[int(i) for i in num]
    print(min(number))
    t-=1


