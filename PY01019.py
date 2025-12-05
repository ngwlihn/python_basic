import math
def check(s):
    for i in range(len(s)//2):
        if abs(ord(s[i+1])-ord(s[i]))!=abs(ord(s[-2-i])-ord(s[-1-i])):
            return 0
    return 1
for _ in range(int(input())):
    s=input()
    if check(s)==1:
        print("YES")
    else:
        print("NO")