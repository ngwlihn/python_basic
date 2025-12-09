def check(s):
    sum=0
    for i in range(len(s)-1):
        sum+=int(s[i])
        if abs(int(s[i])- int (s[i+1]))!=2:
            return 0
    sum+=int(s[-1])
    if sum%10!=0:
        return 0
    return 1

for _ in range(int(input())):
    s=input()
    if check(s)==1:
        print("YES")
    else:
        print("NO")
