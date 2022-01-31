import sys
input=sys.stdin.readline

n=int(input())
student=[]
for _ in range(n):
    name, korean, english, math=input().strip().split()
    student.append([-int(korean), int(english), -int(math), name])

student.sort()
for i in range(n):
    print(student[i][3])