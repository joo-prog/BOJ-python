import sys
from collections import deque
input=sys.stdin.readline

r=[]
for i in range(4):
    r.append(list(input().strip()))

n=int(input())

def rotate(tmp, r):
    a=[]
    for i in range(4):
        if tmp[i]==-1:
            deq=deque(r[i])
            deq.rotate(-1)
            a.append(list(deq))
        elif tmp[i]==1:
            deq=deque(r[i])
            deq.rotate(1)
            a.append(list(deq))
        else:
            a.append(r[i])
    return a

for _ in range(n):
    a, b=map(int, input().split())
    tmp=[0, 0, 0, 0]
    tmp[a-1]=b
    for i in range(a-1, 0, -1):
        if r[i][6]!=r[i-1][2]:
            tmp[i-1]=tmp[i]*(-1)
        else:
            break
    for i in range(a-1, 3):
        if r[i][2]!=r[i+1][6]:
            tmp[i+1]=tmp[i]*(-1)
        else:
            break
    r=rotate(tmp, r)

print(int(r[0][0])+int(r[1][0])*2+int(r[2][0])*4+int(r[3][0])*8)