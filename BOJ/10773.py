import sys
from collections import deque
input=sys.stdin.readline
q=deque()

n=int(input())
for _ in range(n):
    k=int(input())
    if k==0:
        q.pop()
    else:
        q.append(k)

if len(q)==0:
    print(0)
else:
    print(sum(q))