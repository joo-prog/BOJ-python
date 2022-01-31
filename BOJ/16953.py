from collections import deque
a, b=map(int, input().split())

q=deque()
q.append([a, 1])
flag=0
while q:
    x, cnt=q.popleft()
    if x==b:
        flag=1
        print(cnt)
        break
    if x*2<=b: 
        q.append([x*2, cnt+1])
    if x*10+1<=b:
        q.append([x*10+1, cnt+1])
if flag==0:
    print(-1)