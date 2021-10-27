import sys
input=sys.stdin.readline

n, m=map(int, input().split())
num_list=list(map(int, input().split()))

for i in range(1, n):
    num_list[i]+=num_list[i-1]

for _ in range(m):
    start, end=map(int, input().split())
    if start==1:
        print(num_list[end-1])
    else:
        print(num_list[end-1]-num_list[start-2])