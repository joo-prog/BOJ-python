import sys
input=sys.stdin.readline
import heapq

t=int(input())
for _ in range(t):
    cnt=0
    min_heap=[]
    max_heap=[]
    visited=[0]*(1000001)
    k=int(input())
    for i in range(k):
        order, num = input().split()
        num=int(num)
        if order=='I':
            heapq.heappush(min_heap, (num, i))
            heapq.heappush(max_heap, (-num, i))
            visited[i]=1
            cnt+=1
        else:
            if cnt==0:
                continue
            if num==-1:
                while min_heap and visited[min_heap[0][1]]==0:
                    heapq.heappop(min_heap)
                if min_heap:
                    visited[min_heap[0][1]]=0
                    heapq.heappop(min_heap)
                    cnt-=1
            else:
                while max_heap and visited[max_heap[0][1]]==0:
                    heapq.heappop(max_heap)
                if max_heap:
                    visited[max_heap[0][1]]=0
                    heapq.heappop(max_heap)
                    cnt-=1
    while min_heap and visited[min_heap[0][1]]==0:
        heapq.heappop(min_heap)
    while max_heap and visited[max_heap[0][1]]==0:
        heapq.heappop(max_heap)
        
    if cnt==0:
        print('EMPTY')
    else:
        print(-max_heap[0][0], min_heap[0][0])