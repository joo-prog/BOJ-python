import sys, heapq
input=sys.stdin.readline
INF=1000000000

n, e=map(int, input().split())
node=[[] for _ in range(n+1)]
for _ in range(e):
    a, b, c=map(int, input().split())
    node[a].append((b, c))
    node[b].append((a, c))
v1, v2=map(int, input().split())

def dijkstra(start, end):
    dp=[INF]*(n+1)
    dp[start]=0
    heap=[]
    heapq.heappush(heap, [0, start])
    while heap:
        w, s=heapq.heappop(heap)
        for e, c in node[s]:
            if dp[e]>w+c:
                dp[e]=w+c
                heapq.heappush(heap, [w+c, e])
    return dp[end]
cnt=min(dijkstra(1, v1)+dijkstra(v1, v2)+dijkstra(v2, n), dijkstra(1, v2)+dijkstra(v2, v1)+dijkstra(v1, n))

print(cnt if cnt<INF else -1)