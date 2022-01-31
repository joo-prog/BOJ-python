import sys
from collections import deque
input=sys.stdin.readline

def bfs(x, mode, n):
    q=deque()
    q.append(x)
    weight_sum=[-1 for _ in range(n)]
    weight_sum[x]=0

    while q:
        tmp=q.popleft()
        for n, w in node[tmp]:
            if weight_sum[n]==-1:
                weight_sum[n]=weight_sum[tmp]+w
                q.append(n)
    if mode==1:
        return weight_sum.index(max(weight_sum))
    else:
        return max(weight_sum)

n=int(input())
node=[[] for _ in range(n)]

for _ in range(n-1):
    a, b, c=map(int, input().split())
    node[a-1].append([b-1, c])
    node[b-1].append([a-1, c])

index=bfs(0, 1, n)
print(bfs(index, 2, n))