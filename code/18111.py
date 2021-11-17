import sys
input=sys.stdin.readline

n, m, b=map(int, input().split())
li=[]
for i in range(n):
    li.append(list(map(int, input().split())))
height=0
time= 100000000000000000000000
for h in range(257):
    one=0
    two=0
    for i in range(n):
        for j in range(m):
            if li[i][j]<h:
                two+=h-li[i][j]
            else:
                one+=li[i][j]-h
    if two>one+b:
        continue
    tmp_time=one*2+two
    if tmp_time<=time:
        time=tmp_time
        height=h
print(time, height)