import sys
input=sys.stdin.readline

m=int(input())
s=set()
for _ in range(m):
    order=input().split()
    if order[0]=='add':
        order[1]=int(order[1])
        s.add(order[1])
    elif order[0]=='remove':
        order[1]=int(order[1])
        if order[1] in s:
            s.remove(order[1])
    elif order[0]=='check':
        order[1]=int(order[1])
        if order[1] in s:
            print(1)
        else:
            print(0)
    elif order[0]=='toggle':
        order[1]=int(order[1])
        if order[1] in s:
            s.remove(order[1])
        else:
            s.add(order[1])
    elif order[0]=='all':
        s=set([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
    else:
        s=set()