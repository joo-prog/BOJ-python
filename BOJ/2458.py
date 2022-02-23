import sys
from collections import deque
input=sys.stdin.readline

n, m=map(int, input().split())
small=[[] for _ in range(n+1)]
big=[[] for _ in range(n+1)]

for _ in range(m):
    a, b=map(int, input().split())
    big[a].append(b)
    small[b].append(a)

cnt=0
for i in range(1, n+1):
    q=deque()
    q.append(i)
    li=[0]*(n+1)
    while q:
        x=q.popleft()
        for a in small[x]:
            if li[a]==0:
                li[a]=1
                q.append(a)
    q.append(i)
    while q:
        x=q.popleft()
        for a in big[x]:
            if li[a]==0:
                li[a]=1
                q.append(a)
    if sum(li)==n-1:
        cnt+=1

print(cnt)