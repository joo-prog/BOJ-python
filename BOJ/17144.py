import sys
input=sys.stdin.readline

r, c, t=map(int, input().split())

room=[]
clean_up=-1

for i in range(r):
    room.append(list(map(int, input().split())))
    if room[i][0]==-1:
        if clean_up==-1:
            clean_up=i
            clean_down=i+1

def spread():
    dx=[-1, 1, 0, 0]
    dy=[0, 0, -1, 1]
    tmp_room=[[0]*c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if room[i][j]!=0 and room[i][j]!=-1:
                cnt=0
                tmp=room[i][j]//5
                for k in range(4):
                    tmp_x=i+dx[k]
                    tmp_y=j+dy[k]
                    if 0<=tmp_x<r and 0<=tmp_y<c and room[tmp_x][tmp_y]!=-1:
                        cnt+=1
                        tmp_room[tmp_x][tmp_y]+=tmp
                room[i][j]-=(tmp*cnt)
    for i in range(r):
        for j in range(c):
            room[i][j]+=tmp_room[i][j]

def clean_up_():
    dx=[0, -1, 0, 1]
    dy=[1, 0, -1, 0]
    tmp_x=clean_up
    tmp_y=0
    tmp=0
    for i in range(4):
        while True:
            tmp_x+=dx[i]
            tmp_y+=dy[i]
            if 0<=tmp_x<r and 0<=tmp_y<c and room[tmp_x][tmp_y]!=-1:
                tmp, room[tmp_x][tmp_y]=room[tmp_x][tmp_y], tmp
            else:
                tmp_x-=dx[i]
                tmp_y-=dy[i]
                break
        
def clean_down_():
    dx=[0, 1, 0, -1]
    dy=[1, 0, -1, 0]
    tmp_x=clean_down
    tmp_y=0
    tmp=0
    for i in range(4):
        while True:
            tmp_x+=dx[i]
            tmp_y+=dy[i]
            if 0<=tmp_x<r and 0<=tmp_y<c and room[tmp_x][tmp_y]!=-1:
                tmp, room[tmp_x][tmp_y]=room[tmp_x][tmp_y], tmp
            else:
                tmp_x-=dx[i]
                tmp_y-=dy[i]
                break

for _ in range(t):
    spread()
    clean_up_()
    clean_down_()

res=0
for i in range(r):
    for j in range(c):
        if room[i][j]!=0 and room[i][j]!=-1:
            res+=room[i][j]

print(res)
        