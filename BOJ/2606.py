import sys
input=sys.stdin.readline

cnt=0
def dfs(s):
    global cnt
    visited[s]=1
    for i in g[s]:
        if visited[i]==0:
            dfs(i)
            cnt+=1

n=int(input())
p=int(input())

g=[[]*n for _ in range(n+1)]
visited=[0]*(n+1)

for _ in range(p):
    a, b=map(int,input().split())
    g[a].append(b)
    g[b].append(a)

dfs(1)
print(cnt)