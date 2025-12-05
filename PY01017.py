for _ in range (int(input())):
    s=input()
    cnt=1
    ls=[]
    for i in range(1,len(s)):
        if s[i-1]==s[i]:
            cnt+=1
        else:
            ls.append(cnt)
            ls.append(s[i-1])
            cnt=1
    ls.append(cnt)
    ls.append(s[-1])
    print(''.join(map(str,ls)))