n, m, k=map(int, input().split())
li=list(map(int, input().split()))

li.sort()
result=0

cnt=0

while True:
    for i in range(k):
        if cnt==m:
            break
        result+=li[-1]
        cnt+=1
    if cnt==m:
        break
    result+=li[-2]
    cnt+=1

print(result)