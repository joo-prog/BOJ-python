import sys
import heapq
input=sys.stdin.readline

n=int(input())
m=int(input())
MAX_NUM=1000000000

price=[MAX_NUM]*(n+1)
city=[[] for _ in range(n+1)]

for _ in range(m):
    a, b, c=map(int, input().split())
    city[a].append((b,c))

start, end=map(int, input().split())

heap=[]
heapq.heappush(heap, [0, start])
while heap:
    w, e=heapq.heappop(heap)
    if price[e]<w:
        continue
    for a, b in city[e]:
        if price[a]>w+b:
            price[a]=w+b
            heapq.heappush(heap, [w+b, a])

print(price[end])