import sys
input=sys.stdin.readline

n=int(input())

matrix=[]
for i in range(n):
    matrix.append(list(map(int, input().strip())))

def recursion(i, j, tmp_cnt):
    matrix[i][j]=0
    tmp_cnt+=1
    if i!=n-1:
        if matrix[i+1][j]==1:
            tmp_cnt=recursion(i+1, j, tmp_cnt)
    if i!=0:
        if matrix[i-1][j]==1:
            tmp_cnt=recursion(i-1, j, tmp_cnt)
    if j!=n-1:
        if matrix[i][j+1]==1:
            tmp_cnt=recursion(i, j+1, tmp_cnt)
    if j!=0:
        if matrix[i][j-1]==1:
            tmp_cnt=recursion(i, j-1, tmp_cnt)
    return tmp_cnt
    
cnt_apt=[]

for i in range(n):
    for j in range(n):
        if matrix[i][j]==1:
            cnt_apt.append(recursion(i,j, 0))

print(len(cnt_apt))
cnt_apt.sort()
for num in cnt_apt:
    print(num)