import sys
input=sys.stdin.readline

n, k = map(int, input().split())
stuff=[]
for i in range(n):
    w, v=map(int, input().split())
    stuff.append((w, v))

stuff.sort()
weight=[0]*(k+1)
for w, v in stuff:
    for i in range(k, w-1, -1):
        weight[i]=max(weight[i], weight[i-w]+v)
print(weight[k])