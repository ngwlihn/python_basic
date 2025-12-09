def check(n):
    i=1
    while i<=1000:
        i+=1
        if (n%7==0):
            return n
        else:
            n+= int(str(n)[::-1])
    return -1

for _ in range(int(input())):
    n=int(input())
    print(check(n))