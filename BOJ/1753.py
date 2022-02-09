import sys
import heapq
input=sys.stdin.readline

INF=int(1e9)
V, E = map(int, input().split())
k=int(input())
edges=[[] for _ in range(V+1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    edges[u].append((v, w))

min_v=[INF]*(V+1)
heap=[]
def dijkstra(k):
    # (k, 0)하면 시간초과남..
    # 동일하게 앞에서부터 비교해서 그렇다고 함
    heapq.heappush(heap, (0, k))
    min_v[k]=0
    while heap:
        s_w, s_v = heapq.heappop(heap)
        if min_v[s_v]<s_w:
            continue
        for v, w in edges[s_v]:
            tmp_w=s_w+w
            if min_v[v]>tmp_w:
                min_v[v]=tmp_w
                heapq.heappush(heap, (tmp_w, v))

dijkstra(k)

for i in range(1, V+1):
    if min_v[i]==INF:
        print('INF')
    else:
        print(min_v[i])