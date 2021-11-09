import sys
input=sys.stdin.readline
from collections import deque

str=input().strip('\n')

while str!='.':
    q=deque()
    str=list(str)
    flag=0
    for i in range(len(str)):
        if (str[i]=='(') or (str[i]=='['):
            q.append(str[i])
        elif str[i]==')':
            if len(q)==0:
                print('no')
                flag=1
                break
            tmp=q.pop()
            if (tmp!='('):
                flag=1
                print('no')
                break
        elif str[i]==']':
            if len(q)==0:
                print('no')
                flag=1
                break
            tmp=q.pop()
            if (tmp!='['):
                flag=1
                print('no')
                break
    if flag==0:
        if len(q)!=0:
            print('no')
        else:
            print('yes')
    str=input().strip('\n')