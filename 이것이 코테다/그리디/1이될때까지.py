n, k=map(int, input().split())
cnt=0
while n>=k:
    if n%k==0:
        n=n//k
    else:
        n-=1
    cnt+=1
print(n+cnt-1)