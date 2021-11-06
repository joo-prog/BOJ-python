import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)
n, m=map(int, input().split())

g=[[] for _ in range(n+1)]
visited=[0]*(n+1)
for _ in range(m):
    s, e=map(int, input().split())
    g[s].append(e)
    g[e].append(s)

def dfs(num):
    visited[num]=1
    
    for i in g[num]:
        if visited[i]==0:
            dfs(i)

cnt=0
for j in range(1, n+1):
    if visited[j]==0:
        dfs(j)
        cnt+=1

print(cnt)
