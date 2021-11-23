import sys
input=sys.stdin.readline

r, c=map(int, input().split())
li=[]
for _ in range(r):
    li.append(list(input().strip()))

q=set()
q.add((0, 0, li[0][0]))
dx=[-1, 1, 0, 0]
dy=[0, 0, -1, 1]
max_num=0
def bfs():
    global max_num, r, c
    while q:
        x, y, tmp_visit=q.pop()

        for i in range(4):
            tmp_x=x+dx[i]
            tmp_y=y+dy[i]
            flag=0
            if 0<=tmp_x<c and 0<=tmp_y<r:
                if li[tmp_y][tmp_x] not in tmp_visit:
                    flag=1
                    q.add((tmp_x, tmp_y, tmp_visit+li[tmp_y][tmp_x]))
                if flag==0:
                    max_num=max(max_num, len(tmp_visit))
bfs()
print(max_num)