n=input().strip()
x=int(ord(n[0])-ord('a'))+1
y=int(n[1])

dx=[-2, -1, 2, 1, -2, -1, 1, 2]
dy=[-1, -2, -1, -2, 1, 2, 2, 1]
cnt=0
for i in range(8):
    tmp_x=x+dx[i]
    tmp_y=y+dy[i]
    if 1<=tmp_x<=8 and 1<=tmp_y<=8:
        cnt+=1
print(cnt)