import sys
input=sys.stdin.readline

T=int(input())

for i in range(T):
    H, W, N=map(int,input().split())

    floor=N%H
    unit=N//H

    if floor==0:
        floor=H
        unit-=1
        
    print(floor*100+unit+1)