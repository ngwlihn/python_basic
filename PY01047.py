import math
def isprime(n):
    if n<2: return 0
    if n==2: return 1
    for i in range(2,int(math.sqrt(n))):
        if n%i==0: return 0
    return 1
for _ in range(int(input())):
    s=input()
    t=s[-4:]
    t=int(t)
    if isprime(t)==1:
        print("YES")
    else:
        print("NO")
