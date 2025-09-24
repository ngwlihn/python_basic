def check(s):
    t= len(s)
    for i in range(0,t-2):
        if s[i]!=s[i+2]:
            return 0
    return 1
t=int(input())
while t>0:
    s=input()
    if check(s)==1:
        print("YES\n")
    else:
        print("NO\n")
    t-=1

        