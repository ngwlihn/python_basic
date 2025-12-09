import math

l,r= map(int,input().split())
for i in range(l,r-1):
    for j in range(i+1,r):
        for k in range(j+1,r+1):
            if math.gcd(i,k)==math.gcd(i,j)==math.gcd(j,k)==1:
                print('('+ str(i)+', '+str(j)+', '+str(k)+')')