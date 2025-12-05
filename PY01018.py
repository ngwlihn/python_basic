# Sử dụng dấu nháy đơn để định nghĩa mỗi ký tự là một chuỗi/ký tự
p = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '_', '.']
while True:
    s=input()
    t=s.split(maxsplit=1)
    k=int(''.join(t[0]))
    if k==0:
        break
    else:
        a=list(t[1])
        for i in range(len(a)):
            a[i]=p[(p.index(a[i])+k)%28]
        print(''.join(a)[::-1])
    