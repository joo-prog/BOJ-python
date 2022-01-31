import sys
input=sys.stdin.readline

n, m=map(int, input().split())
matrix=[]
for i in range(n):
    tmp=list(map(int, input().split()))
    for j in range(1, n):
        tmp[j]+=tmp[j-1]
    matrix.append(tmp)

for i in range(m):
    x1, y1, x2, y2=map(int, input().split())
    res=0
    for i in range(x1-1, x2):
        res+=matrix[i][y2-1]
        if y1!=1:
            res-=matrix[i][y1-2]
    print(res)