import sys
input=sys.stdin.readline

n=int(input())

stack=[]

for i in range(n):
    order=input().strip().split()
    if order[0]=='pop':
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())

    elif order[0]=='size':
        print(len(stack))

    elif order[0]=='empty':
        if len(stack)==0:
            print(1)
        else:
            print(0)

    elif order[0]=='top':
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])
            
    else:
        stack.append(order[1])