import sys
from collections import Counter
input=sys.stdin.readline

n=int(input())
li=[]
for _ in range(n):
    li.append(int(input()))

mode=Counter(li).most_common()
mode_li=[]
for num in mode:
    if num[1]==mode[0][1]:
        mode_li.append(num[0])
    else:
        break
mode_li.sort()

li.sort()
print(round(sum(li)/n))
print(li[n//2])

if len(mode_li)==1:
    print(mode_li[0])
else:
    print(mode_li[1])
print(max(li)-min(li))