import sys
from collections import deque
input=sys.stdin.readline
n, m=map(int, input().split())
ladder1=[]
ladder2=[]
snake1=[]
snake2=[]

for _ in range(n):
    x, y=map(int, input().split())
    ladder1.append(x)
    ladder2.append(y)
for _ in range(m):
    x, y=map(int, input().split())
    snake1.append(x)
    snake2.append(y)

q=deque()
q.append([1, 0])
min_num=100
visited=[0]*101
visited[1]=1

while q:
    x, cnt=q.popleft()
    for i in range(1, 7):
        x+=1
        if x>100:
            break
        elif x==100:
            if cnt+1<min_num:
                min_num=cnt+1
                break
        elif x in ladder1:
            if visited[ladder2[ladder1.index(x)]]==0:
                visited[ladder2[ladder1.index(x)]]=1
                q.append([ladder2[ladder1.index(x)], cnt+1])
        elif x in snake1:
            if visited[snake2[snake1.index(x)]]==0:
                visited[snake2[snake1.index(x)]]=1
                q.append([snake2[snake1.index(x)], cnt+1])
        else:
            if visited[x]==0:
                visited[x]=1
                q.append([x, cnt+1])
print(min_num)