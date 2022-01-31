import sys
sys.setrecursionlimit(10**6)
T=int(input())

def dfs(x):
    global res
    visited[x]=1
    cycle.append(x)
    tmp=array[x]

    if visited[tmp-1]:
        if tmp-1 in cycle:
            res+=cycle[cycle.index(tmp-1):]
        return
    else:
        dfs(tmp-1)

for _ in range(T):
    n=int(input())
    array=list(map(int, input().split()))
    visited=[0]*n
    res=[]
    for i in range(n):
        if not visited[i]:
            cycle=[]
            dfs(i)
    print(n-len(res))