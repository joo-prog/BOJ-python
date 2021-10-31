import sys
input=sys.stdin.readline

n=int(input())

student=[]

for _ in range(n):
    student.append(list(map(int, input().split())))

list=[]

for i in range(n):
    cnt=0
    for j in range(n):
        if i==j:
            continue
        if (student[i][0]<student[j][0])&(student[i][1]<student[j][1]):
            cnt+=1
    list.append(cnt+1)

for i in range(n):
    print(list[i], end=' ')