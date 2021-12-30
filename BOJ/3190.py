import sys
input=sys.stdin.readline

n=int(input())
k=int(input())

board=[[0]*n for _ in range(n)]
for _ in range(k):
    x, y=map(int, input().split())
    board[x-1][y-1]=-1 #apple

l=int(input())
rotate=[]
for _ in range(l):
    rotate.append(list(input().split()))
tmp_idx=0
tail_tmp_idx=0

board[0][0]=1 #snake
tail_x, tail_y=0, 0
head_x, head_y=0, 0

dx=[0, -1, 0, 1]
dy=[1, 0, -1, 0]
head_rotate_idx=0
tail_rotate_idx=0

time=0
tail_time=0

def idx_rotate(s, idx):
    if s=='L':
        idx+=1
        if idx==4:
            idx=0
    elif s=='D':
        idx-=1
        if idx==-1:
            idx=3
    return idx

def snake_rotate(s):
    global rotate, time, tmp_idx, tail_x, tail_y, dx, dy, tail_tmp_idx, head_rotate_idx, tail_rotate_idx
    if s=='h':
        r_time=int(rotate[tmp_idx][0])
        if r_time==time:
            head_rotate_idx=idx_rotate(rotate[tmp_idx][1], head_rotate_idx)
            tmp_idx+=1
    elif s=='t':
        r_time=int(rotate[tail_tmp_idx][0])
        board[tail_x][tail_y]=0
        if r_time==tail_time:
            tail_rotate_idx=idx_rotate(rotate[tail_tmp_idx][1], tail_rotate_idx)
            tail_tmp_idx+=1
        tail_x=tail_x+dx[tail_rotate_idx]
        tail_y=tail_y+dy[tail_rotate_idx]

while True:
    head_x+=dx[head_rotate_idx]
    head_y+=dy[head_rotate_idx]
    time+=1
    if not (0<=head_x<n and 0<=head_y<n):
        break
    if board[head_x][head_y]==-1:
        board[head_x][head_y]=1
    elif board[head_x][head_y]==0:
        board[head_x][head_y]=1
        if tail_tmp_idx<len(rotate):
            snake_rotate('t')
        tail_time+=1
    else:
        break
    if tmp_idx<len(rotate):
        snake_rotate('h')

print(time)