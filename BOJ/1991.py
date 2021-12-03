import sys
input=sys.stdin.readline

n=int(input())
dic={}

for _ in range(n):
    node=list(input().split())
    dic[node[0]]=[node[1], node[2]]

def preorder(start):
    print(start, end='')
    if start in dic.keys():
        for item in dic[start]:
            if item != '.':
               preorder(item)

def inorder(start):
    if start in dic.keys():
        tmp=1
        for item in dic[start]:
            if item !='.':
                inorder(item)
            if tmp==1:
                print(start, end='')
                tmp+=1

def postorder(start):
    if start in dic.keys():
        for item in dic[start]:
            if item !='.':
                postorder(item)
        print(start, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')