import math
n,k=map(int,input().split())
b=10**(k-1)
e=10**(k)
res=[]
for i in range(b,e):
    if math.gcd(n,i)==1:
        res.append(i)
for i in range(0,len(res),10):
    print(' '.join(str(x) for x in res[i:i+10]))