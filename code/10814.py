import sys
input=sys.stdin.readline

n=int(input())

join_list=[]

for i in range(n):
    join=input().strip().split()
    join_list.append([int(join[0]),join[1],i])

join_list.sort(key=lambda x:[x[0],x[2]])

for i in range(n):
    print(join_list[i][0], join_list[i][1])
