from collections import Counter

n=int(input())
card=list(map(int, input().split()))
m=int(input())
num=list(map(int,input().split()))

c=Counter(card)
for num_m in num:
    if num_m in c:
        print(c[num_m], end=' ')
    else:
        print(0, end=' ')
