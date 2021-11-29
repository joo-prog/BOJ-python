from collections import deque
def solution(progresses, speeds):
    answer = []
    q=deque()
    tmp=0
    for i in range(len(speeds)):
        q.append([progresses[i], speeds[i], i+1])

    while q:
        cnt=0
        q_length=len(q)
        for i in range(q_length):
            progress, speed, priority=q.popleft()
            if progress>=100:
                if priority-1==tmp:
                    tmp=priority
                    cnt+=1
                else:
                    q.append([progress, speed, priority])
            else:
                q.append([progress+speed, speed, priority])
                
        if cnt!=0:
            answer.append(cnt)
    
    return answer