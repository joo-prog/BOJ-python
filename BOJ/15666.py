from itertools import combinations_with_replacement

n, m=map(int, input().split())
li=sorted(list(map(int, input().split())))
s=sorted(list(set(combinations_with_replacement(li, m))))

for i in s:
    for j in i:
        print(j, end=' ')
    print()