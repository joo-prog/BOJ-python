n=int(input())
t=[]
p=[]

for _ in range(n):
    a, b=map(int, input().split())
    t.append(a)
    p.append(b)

dp=[0]*(n+1)
max_num=0
for i in range(n-1, -1, -1):
    time=t[i]+i
    if time<=n:
        dp[i]=max(p[i]+dp[time], max_num)
        max_num=dp[i]
    else:
        dp[i]=max_num
print(max_num)