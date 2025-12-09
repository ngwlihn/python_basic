for _ in range(int(input())):
    n=int(input())
    k=2
    res=[]
    while n>1:
        cnt=0
        while n%k==0:
            n//=k
            cnt+=1
        if cnt!=0:
            res.append(f"{k}^{cnt}")
        k+=1
    print('1 * '+ ' * '.join((res)))