import sys
a,k,n= map(int,input().split())
mod=a%k
ar=[]
for i in range (k-mod,n-a+1,k):
    ar.append(i)
if not ar:
    print(-1)
else :
    print(' '.join(map(str,ar)))