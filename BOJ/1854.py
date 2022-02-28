import sys, heapq
input=sys.stdin.readline
INF=1000000000

n, m, k=map(int, input().split())
city=[[] for _ in range(n+1)]

for _ in range(m):
    a, b, c=map(int, input().split())
    city[a].append((b, c))

heap=[]
heapq.heappush(heap, [0, 1])
dp=[[INF]*k for _ in range(n+1)]
dp[1][0]=0

while heap:
    w, x=heapq.heappop(heap)
    for b, c in city[x]:
        if dp[b][k-1]>c+w:
            dp[b][k-1]=c+w
            heapq.heappush(heap, [c+w, b])
            dp[b].sort()

for i in range(1, n+1):
    if dp[i][k-1]==INF:
        print(-1)
    else:
        print(dp[i][k-1])
