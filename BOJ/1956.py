import sys
import heapq
input=sys.stdin.readline
INF=1000000000
v, e=map(int, input().split())
matrix=[[] for _ in range(v+1)]

for _ in range(e):
    a, b, c=map(int, input().split())
    matrix[a].append((b, c))
res=INF
for i in range(1, v+1):
    heap=[]
    heapq.heappush(heap, [0, i])
    tmp=[INF]*(v+1)
    while heap:
        w, x=heapq.heappop(heap)
        if tmp[x]<w:
            continue
        for b, c in matrix[x]:
            if tmp[b]>w+c:
                tmp[b]=w+c
                heapq.heappush(heap, [w+c, b])
    
    if tmp[i]!=INF and res>tmp[i]:
        res=tmp[i]

if res==INF:
    print(-1)
else:
    print(res)