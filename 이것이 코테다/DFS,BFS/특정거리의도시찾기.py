import sys
from collections import deque
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

n, m, k, x=map(int, input().split())
list=[[] for _ in range(n+1)]
min_length=[0]*(n+1)
for i in range(m):
    a, b=map(int, input().split())
    list[a].append(b)
q=deque()
q.append(x)
while q:
    now=q.popleft()
    for next_node in list[now]:
        if next_node==x:
            continue
        if min_length[next_node]==0:
            min_length[next_node]=min_length[now]+1
            q.append(next_node)

flag=0
for i in range(n+1):
    if min_length[i]==k:
        print(i)
        flag=1

if flag==0:
    print(-1)