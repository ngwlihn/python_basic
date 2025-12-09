s=input()
res=[]
res.append(s[-3:])
for i in range(len(s)-3,0,-3):
    if (i-3>0):
        res.append(s[i-3:i])
    else:
        res.append(s[:i])
res.reverse()
print(','.join(res))