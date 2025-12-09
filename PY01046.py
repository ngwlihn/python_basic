def thapHN(a,b,c,n):
    if n==1:
        print (a + '->'+c)
    else:
        thapHN(a,c,b,n-1)
        thapHN(a,b,c,1)
        thapHN(b,a,c,n-1)

n=int(input())
a,b,c='A','B','C'
thapHN(a,b,c,n)