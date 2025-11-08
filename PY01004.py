import math
def is_prime(n):
    if n<2:
        return 0
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return 0
    return 1
def phi(n):
    result=n
    for i in range (2, int(math.sqrt(n))+1):
        if n%i==0:
            while n%i==0:
                n//=i
            result-= result//i
    if n>1:
        result-=result//n
    return result

t =int(input())
while (t>0):
    n=int(input())
    k=phi(n)
    if is_prime(k)==1:
        print("YES")
    else:
        print("NO")
    t-=1