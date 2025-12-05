n=int(input())
a=list(map(int,input().split()))
stack=[]
for i in range(n):
    if not stack:
        stack.append(a[i])
        continue
    if (stack[-1]+a[i])%2==0:
        stack.pop()
    else:
        stack.append(a[i])
print(len(stack))