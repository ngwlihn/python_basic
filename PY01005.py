def check(n):
    for x in range(n):
        if (x!='4' and x!='7'):
            return 0
    return 1

t=int(input())
while t>0:
    s = input()
    
    if check(s)==1:
        print("YES")
    else:
        print("NO")
    t-=1
