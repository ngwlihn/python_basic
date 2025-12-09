import sys
s = "ABC"
res = [] 
t = []  
def Try(i, n):
    global t, res 
    for char in s: 
        t.append(char)
        if len(t) == n:
            res.append("".join(t))  
        else:
            Try(i + 1, n) 
        t.pop() 

def check(s):
    cnt={'A':0 ,'B':0,'C':0}
    for char in s:
        cnt[char]+=1
    if cnt['A']==0 or cnt['B']==0 or cnt['C']==0:
        return 0
    if cnt['A'] <= cnt['B']and cnt['B']<= cnt['C']:
        return 1
    return 0
n=int(input())
for i in range(3,n+1):
    Try(0,i)
for j in res:
    if check(j)==1:
        print(j)
