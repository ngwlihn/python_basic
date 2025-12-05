t =int(input())
while t>0:
    t-=1
    a, b =map(str,input().split())
    s = input().split()
    if(len(s) > 1):
        x1, x2 = s[0], s[1]
    else:
        x1 = s[0]
        x2 = input()
    x=x1.replace(b,a)
    y=x2.replace(b,a)
    z=x1.replace(a,b)
    g=x2.replace(a,b)
    ma=int(x)+int(y)
    mi=int(z)+int(g)
    print(min(mi,ma),max(mi,ma))