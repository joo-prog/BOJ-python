import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

n=int(input())
tree=[[] for _ in range(n+1)]
parent=[0]*(n+1)

for _ in range(n-1):
    a, b=map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

def dfs(root):
    for s in tree[root]:
        if parent[s]==0 and s!=1:
            parent[s]=root
            dfs(s)
            
dfs(1)
for i in range(2, n+1):
    print(parent[i])