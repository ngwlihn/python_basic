def ok(s,k):
    for i in range (0,k):
        if int(s[i])>=int(s[i+1]): return 0
    for i in range (k,len(s)-1):
        if int(s[i])<=int(s[i+1]): return 0
    return 1
def check(s):
    if len(s)<3: return 0
    for i in range(len(s)):
        if ok(s,i)==1:
            return 1
    return 0

for _ in range(int(input())):
    n=input()
    if check(n)==1:
        print("YES")
    else:
        print("NO")