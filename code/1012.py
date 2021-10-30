import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

T=int(input())

def dfs(i, j):
    matrix[i][j]=0
    if i!=N-1:
        if matrix[i+1][j]==1:
            dfs(i+1, j)
    if i!=0:
        if matrix[i-1][j]==1:
            dfs(i-1, j)
    if j!=M-1:
        if matrix[i][j+1]==1:
            dfs(i, j+1)
    if j!=0:
        if matrix[i][j-1]==1:
            dfs(i, j-1)

for _ in range(T):
    M, N, K=map(int,input().split())
    matrix=[[0]*M for _ in range(N)]
    for _ in range(K):
        X, Y=map(int,input().split())
        matrix[Y][X]=1
    cnt=0
    for i in range(N):
        for j in range(M):
            if matrix[i][j]==1:
                dfs(i, j)
                cnt+=1
    print(cnt)