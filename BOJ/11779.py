import sys, heapq
input=sys.stdin.readline
INF=1000000000

n=int(input())
m=int(input())
heap=[]
city=[[] for _ in range(n+1)]

for _ in range(m):
    a, b, c=map(int, input().split())
    city[a].append((b, c))

start, end=map(int, input().split())

heapq.heappush(heap, [0, start, [start]])
li=[INF]*(n+1)
way=[]
li[start]=0
while heap:
    w, tmp_s, tmp_way = heapq.heappop(heap)
    if li[tmp_s]<w:
        continue
    if tmp_s==end:
        way=tmp_way
        li[tmp_s]=w
        continue
    for tmp_end, tmp_w in city[tmp_s]:
        if li[tmp_end]>w+tmp_w:
            li[tmp_end]=w+tmp_w
            tmp_tmp_way=tmp_way[:]
            tmp_tmp_way.append(tmp_end)
            heapq.heappush(heap, [w+tmp_w, tmp_end, tmp_tmp_way])

print(li[end])
print(len(way))
for i in way:
    print(i, end=' ')