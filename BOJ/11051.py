n, k=map(int, input().split())

res=1
for i in range(k):
    res*=n
    n-=1

res2=1
for i in range(1, k+1):
    res2*=i
print(res//res2%10007)