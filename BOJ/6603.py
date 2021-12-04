import sys
from itertools import combinations
input=sys.stdin.readline

while True:
    li=list(map(int, input().split()))
    if li[0]==0:
        break
    
    for i in list(combinations(li[1:len(li)], 6)):
        for j in i:
            print(j, end=' ')
        print()
    print()