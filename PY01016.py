for _ in range(int(input())):
    s=input()
    a=[]
    for i in range(1,len(s),2):
        a.append(s[i-1]*int(s[i]))
    print(''.join(a))