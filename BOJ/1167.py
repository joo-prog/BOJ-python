import sys
from collections import deque
input=sys.stdin.readline

n=int(input())
node=[[] for _ in range(n+1)]
for _ in range(n):
    info=list(map(int, input().split()))
    i=1
    while info[i]!=-1:
        node[info[0]].append([info[i], info[i+1]])
        i+=2

def bfs(x, mode):
    global n
    q=deque()
    q.append(x)
    c=[-1]*(n+1)
    c[x]=0

    while q:
        tmp=q.popleft()
        for e, w in node[tmp]:
            if c[e]==-1:
                c[e]=c[tmp]+w
                q.append(e)

    if mode==1:
        return c.index(max(c))
    elif mode==2:
        return max(c)

print(bfs(bfs(1, 1), 2))
