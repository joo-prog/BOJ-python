n, k=map(int, input().split())
coin=[]
for _ in range(n):
    coin.append(int(input()))

cnt=0
i=n-1
while True:
    if k==0:
        break
    if coin[i]<=k:
        cnt+=(k//coin[i])
        k=k-(coin[i]*(k//coin[i]))
    
    i-=1
print(cnt)