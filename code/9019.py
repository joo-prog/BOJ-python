import sys
from collections import deque
input=sys.stdin.readline

n=int(input())

def bfs(start, end):
    queue=deque()
    queue.append([start,''])
    visited[start]=1

    while queue:
        num, order=queue.popleft()

        if num==end:
            print(order, end='\n')
            break
        
        if visited[num*2%10000]==0:
            visited[num*2%10000]=1
            queue.append([num*2%10000, order+'D'])

        if num==0:
            tmp=9999
        else:
            tmp=num-1
        if visited[tmp]==0:
            visited[tmp]=1
            queue.append([tmp,order+'S'])

        if visited[(num%1000*10)+num//1000]==0:
            visited[(num%1000*10)+num//1000]=1
            queue.append([(num%1000*10)+num//1000, order+'L'])

        if visited[(num%10*1000)+num//10]==0:
            visited[(num%10*1000)+num//10]=1
            queue.append([(num%10*1000)+num//10, order+'R'])

for _ in range(n):
    start, end = map(int,input().split())
    visited=[0]*10000
    bfs(start, end)
