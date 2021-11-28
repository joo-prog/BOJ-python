import sys
input=sys.stdin.readline

n=int(input())

stack=[]
push_pop=[]
stack_num=1
flag=0

for i in range(n):
    sequence=int(input())
    if len(stack)==0:
        stack.append(stack_num)
        stack_num+=1
        push_pop.append('+')

    if sequence>=stack[-1]:
        while sequence!=stack[-1]:
            stack.append(stack_num)
            stack_num+=1
            push_pop.append('+')
        push_pop.append('-')
        stack.pop()

    elif sequence<stack[-1]:
        flag=1

if flag==1:
    print('NO')
else:
    for i in range(len(push_pop)):
        print(push_pop[i])
