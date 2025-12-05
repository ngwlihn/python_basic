import math

def check(n):
    s=str(n)
    sum=0
    for i in s:
        sum+=int(i)
    if sum<2:
        return 0
    if sum==2: 
        return 1
    for i in range(2,int(math.sqrt(sum))+1):
        if sum%i==0:
            return 0
    return 1
t=int(input())
while t>0:
    t-=1
    a,b=map(int,input().split())
    x=math.gcd(a,b)
    if check(x)==1:
        print("YES")
    else:
        print("NO")
