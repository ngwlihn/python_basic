t=int(input())
while t>0:
    t-=1
    cs=int(input())
    s=input()
    res=int(s,2)
    if (cs==2):
        print(bin(res)[2:])
    elif (cs==8):
        print(oct(res)[2:])
    elif (cs==16):
        print(hex(res)[2:].upper())
    else:
        rs=""
        while (res>0):
            res,mod=divmod(res,cs)
            rs+=str(mod)
        print(rs[::-1])