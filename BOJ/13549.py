import heapq
n, k=map(int, input().split())
if n==k:
    print(0)
    exit(0)

heap=[]
heapq.heappush(heap, [0, n])
dp=[1000000000]*100001

while heap:
    t, tmp=heapq.heappop(heap)
    if dp[tmp]<t:
        continue
    for i in [tmp-1, tmp+1, 2*tmp]:
        if 0<=i<=100000:
            if i!=2*tmp and dp[i]>t+1:
                dp[i]=t+1
                heapq.heappush(heap, [t+1, i])
            elif i==2*tmp and dp[i]>t:
                dp[i]=t
                heapq.heappush(heap, [t, i])

print(dp[k])