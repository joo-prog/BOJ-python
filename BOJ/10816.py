from collections import Counter

def binary_search(num):
    left=0
    right=len(card_list)-1
    mid=(left+right)//2
    while left<=right:
        if card_list[mid][0]<num:
            left=mid+1
        elif card_list[mid][0]>num:
            right=mid-1
        else:
            return card_list[mid][1]
        mid=(left+right)//2
    return 0

n=int(input())
card=list(map(int, input().split()))
m=int(input())
num=list(map(int,input().split()))

c=Counter(card)
card_list=[]
for key, value in c.items():
    card_list.append([key, value])
card_list.sort(key=lambda x:x[0])

for i in range(m):
    tmp=binary_search(num[i])
    print(tmp, end=' ')

