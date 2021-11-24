import sys
input=sys.stdin.readline

n=int(input())
g=[[] for _ in range(n)]

li=[[0]*n for _ in range(n)]

for i in range(n):
    tmp=list(map(int, input().split()))
    for j in range(n):
        if tmp[j]==1:
            g[i].append(j)

def dfs(start, tmp, visited):
    for i in g[tmp]:
        li[start][i]=1
        if visited[i]==1:
            continue
        visited[i]=1
        dfs(start, i, visited)

for i in range(n):
    visited=[0]*n
    visited[i]=1
    dfs(i, i, visited)

for i in range(n):
    for j in range(n):
        print(li[i][j], end=' ')
    print()
