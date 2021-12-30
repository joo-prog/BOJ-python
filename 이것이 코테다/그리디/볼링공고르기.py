n, m=map(int, input().split())
li=list(map(int, input().split()))

weight=[0]*(m+1)
for i in range(n):
    weight[li[i]]+=1

result=0
for i in range(1, m):
    result+=(sum(weight[i+1:])*weight[i])

print(result)