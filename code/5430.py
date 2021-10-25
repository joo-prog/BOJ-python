import sys
input=sys.stdin.readline
from collections import deque

T=int(input())

for _ in range(T):
    x=[]
    p=list(input().strip())
    n=int(input())
    tmp=input().strip()
    x=deque(tmp[1:-1].split(','))
    flag, cnt=0,0
    for i in range(len(p)):
        if len(x)==0:
            flag=1
            break
        if p[i]=='R':
            cnt+=1
        else:
            if (tmp=='[]'):
                flag=1
                break
            if cnt%2==1:
                x.pop()
            else:
                x.popleft()

    if (flag==1):
        print('error')
    else:
        if cnt%2==1:
            x.reverse()
        print('['+','.join(x)+']')