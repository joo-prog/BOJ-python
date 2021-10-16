import sys
input=sys.stdin.readline

n=int(input())

stack=[]

def push(num):
    stack.append(num)

def pop():
    if len(stack)!=0:
        print(stack[len(stack)-1])
        del stack[len(stack)-1]
    else:
        print(-1)

def size():
    print(len(stack))

def empty():
    if len(stack)==0:
        print(1)
    else:
        print(0)

def top():
    if len(stack)==0:
        print(-1)
    else:
        print(stack[len(stack)-1])

for i in range(n):
    order=input().strip()
    if order=='pop':
        pop()
    elif order=='size':
        size()
    elif order=='empty':
        empty()
    elif order=='top':
        top()
    else:
        _, num=order.split()
        push(num)
