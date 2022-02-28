import sys, heapq
input=sys.stdin.readline
INF=1000000000

n, m=map(int, input().split())
matrix=[]
for _ in range(m):
    matrix.append(list(input().strip()))

dx=[0, 0, -1, 1]
dy=[-1, 1, 0, 0]

dp=[[INF]*n for _ in range(m)]
heap=[]
heapq.heappush(heap, [0, 0, 0])
while heap:
    wall, x, y = heapq.heappop(heap)
    if dp[x][y]<wall:
        continue
    for i in range(4):
        tmp_x=x+dx[i]
        tmp_y=y+dy[i]
        if 0<=tmp_x<m and 0<=tmp_y<n:
            if matrix[tmp_x][tmp_y]=='0' and dp[tmp_x][tmp_y]>wall:
                dp[tmp_x][tmp_y]=wall
                heapq.heappush(heap, [wall, tmp_x, tmp_y])
            elif matrix[tmp_x][tmp_y]=='1' and dp[tmp_x][tmp_y]>(wall+1):
                dp[tmp_x][tmp_y]=wall+1
                heapq.heappush(heap, [wall+1, tmp_x, tmp_y])
                
if dp[m-1][n-1]==INF:
    print(0)
else:
    print(dp[m-1][n-1])