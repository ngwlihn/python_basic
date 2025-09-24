t = int(input())
while t>0:
    n = int(input())
    res = []
    k = 2
    while n > 1:
        count = 0
        while n % k == 0:
            count += 1
            n //= k
        if count > 0:
            res.append(f"{k}^{count}")
        k += 1
    print("1 * " + " * ".join(res))
    t-=1
