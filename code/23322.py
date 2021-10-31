n, k=map(int, input().split())

a=list(map(int, input().split()))
cnt=0
for i in range(n):
    if a[i]!=a[0]:
        break
    cnt+=1

print(sum(a)-a[0]*n, len(a)-cnt)