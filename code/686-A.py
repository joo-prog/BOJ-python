n=int(input())

student=list(map(int, input().split()))

x, y=map(int, input().split())

student.sort()
cnt=0
s_stu=int(n*(x/100)+0.5)

for i in range(n):
    if student[i]>=y:
        break
    cnt+=1

print(s_stu, n-cnt)