import sys
input=sys.stdin.readline

t=int(input())
for _ in range(t):
    li=[1,1,1,2,2,3,4,5,7,9]
    n=int(input())
    for i in range(10, n):
        li.append(li[i-1]+li[i-5])
    print(li[n-1])