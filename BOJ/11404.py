import sys
input=sys.stdin.readline

n=int(input())
m=int(input())

INF=int(1e9)
res=[[INF]*(n+1) for _ in range(n+1)]
for i in range(1, n+1):
    res[i][i]=0

for _ in range(m):
    a, b, c = map(int, input().split())
    if res[a][b]>c:
        res[a][b]=c

for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            res[j][k]=min(res[j][k], res[j][i]+res[i][k])

for i in range(1, n+1):
    for j in range(1, n+1):
        if res[i][j]==INF:
            print(0, end=" ")
        else:
            print(res[i][j], end=" ")
    print()