s1=[2,4,6,8]
s2=[0,2,4,6,8]

for _ in range(int(input())):
    n=input()
    a=s1[:]
    for i in s1:
        for j in s2:
            a.append(''.join(str(i))+''.join(str(j)))
    t=len(a)
    for i in range(4,t):
        for j in s2:
            a.append(''.join(str(a[i]))+''.join(str(j)))
    for i in a:
        s=''.join(str(i))+''.join(str(i))[::-1]
        if int(s)<int(n):
            print(s,end=" ")
        else:
            break
    print()
