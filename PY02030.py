# Hàm kiểm tra số nguyên tố
def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

# Nhập kích thước ma trận
n, m = map(int, input().split())

# Nhập ma trận A
A = [list(map(int, input().split())) for _ in range(n)]

# Tạo ma trận kết quả
for i in range(n):
    for j in range(m):
        if is_prime(A[i][j]):
            A[i][j] = 1
        else:
            A[i][j] = 0

# In ma trận kết quả
for row in A:
    print(*row)
