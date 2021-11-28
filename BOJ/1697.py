from collections import deque
n, m = map(int, input().split())

def bfs(start, end):
    queue=deque()
    queue.append([start,0])
    visited=[0]*100001

    while queue:
        place, num = queue.popleft()

        if place==end:
            print(num)
            break
        
        if place!=0:
            if visited[place-1]==0:
                visited[place-1]=1
                queue.append([place-1, num+1])
        
        if place!=100000:
            if visited[place+1]==0:
                visited[place+1]=1
                queue.append([place+1, num+1])
                
        if 2*place<=100000:
            if visited[2*place]==0:
                visited[2*place]=1
                queue.append([place*2, num+1])
bfs(n, m)