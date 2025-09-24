def lam_tron(n):
    b = 10
    while n >= b:
        r = n % b
        if r >= b // 2:
            n += (b - r)
        else:
            n -= r
        b *= 10
    return n

t = int(input())
for _ in range(t):
    n = int(input())
    print(lam_tron(n))
