import sys
input=sys.stdin.readline

t=int(input())
for _ in range(t):
    n=int(input())
    dic={}
    for _ in range(n):
        clothes = list(input().strip().split())
        if clothes[1] not in dic.keys():
            dic[clothes[1]]=1
        else:
            dic[clothes[1]]+=1
    result=1
    for i in dic.keys():
        result*=(dic[i]+1)
    print(result-1)
