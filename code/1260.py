from collections import deque
import sys
input=sys.stdin.readline

n, m, v=map(int, input().split())
li=[[] for _ in range(n+1)]

for _ in range(m):
    start, end=map(int, input().split())
    li[start].append(end)
    li[end].append(start)
for i in range(1, n+1):
    li[i].sort()

def dfs(start):
    visited[start]=1
    for i in range(len(li[start])):
        if visited[li[start][i]]==0:
            print(li[start][i], end=' ')
            dfs(li[start][i])

def bfs():
    for i in range(len(li[v])):
        q.append([v, li[v][i]])
        visited[li[v][i]]=1
        print(li[v][i], end=' ')
    while q:
        s, e=q.popleft()
        for i in range(len(li[e])):
            if visited[li[e][i]]==0:
                visited[li[e][i]]=1
                print(li[e][i], end=' ')
                q.append([e, li[e][i]])

visited=[0]*(n+1)
print(v, end=' ')
dfs(v)
print()

visited=[0]*(n+1)
visited[v]=1
q=deque()
print (v, end=' ')
bfs()