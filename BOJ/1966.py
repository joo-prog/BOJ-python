import sys
from collections import deque
input=sys.stdin.readline

def print_document(q, m, li_sort, index):
    while q:
        tmp_index, important=q.popleft()
        if important==li_sort[index]:
            if tmp_index!=m:
                index+=1
            else:
                print(index+1)
                break
        else:
            q.append([tmp_index, important])

t=int(input())
for _ in range(t):
    n, m=map(int,input().split())
    li=list(map(int, input().split()))
    li_sort=sorted(li, reverse=True)
    index=0
    q=deque()
    for i in range(n):
        q.append([i, li[i]])
    print_document(q, m, li_sort, index)
