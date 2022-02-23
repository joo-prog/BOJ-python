import sys
import heapq
input=sys.stdin.readline
MAX_INT=1000000000

n, m, x=map(int, input().split())
city=[[] for _ in range(n+1)]
for _ in range(m):
    a, b, c=map(int, input().split())
    city[a].append((b, c))

def dijkstra(s, e):
    dp=[MAX_INT]*(n+1)
    heap=[]
    heapq.heappush(heap, [0, s])
    while heap:
        w, x=heapq.heappop(heap)
        if dp[x]<w:
            continue
        for y, tmp_w in city[x]:
            if dp[y]>tmp_w+w:
                dp[y]=tmp_w+w
                heapq.heappush(heap, [tmp_w+w, y])
    return dp[e]

li=[0]*(n+1)
for i in range(1, n+1):
    if i!=x:
        li[i]+=dijkstra(i, x)
        li[i]+=dijkstra(x, i)

print(max(li))