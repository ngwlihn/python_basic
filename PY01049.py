import math
def isprime(n):
    if n<2: return 0
    if n==2: return 1
    for i in range(2,int(math.sqrt(n))):
        if n%i==0: return 0
    return 1
t="2357"
def checkk(s):
    n=0
    no=0
    for i in s:
        n+=1
        if i not in t:
            no+=1
    if no>len(s)-no: return 0
    if isprime(n)==0: return 0
    return 1

for _ in range(int(input())):
    s=input()
    if checkk(s)==1:
        print("YES")
    else:
        print("NO")
    