import sys
input=sys.stdin.readline

def merge_sort(li):
    if len(li)==1:
        return li

    mid=len(li)//2
    left=merge_sort(li[:mid])
    right=merge_sort(li[mid:])
    
    l_left=0
    r_left=0
    sort=[]
    while (l_left!=len(left))|(r_left!=len(right)):
        if l_left==len(left):
            sort.append(right[r_left])
            r_left+=1
        elif r_left==len(right):
            sort.append(left[l_left])
            l_left+=1
        elif left[l_left]<right[r_left]:
            sort.append(left[l_left])
            l_left+=1
        else:
            sort.append(right[r_left])
            r_left+=1

    return sort

n=int(input())
li=[]
sort_li=[]
    
for i in range(n):
    li.append(int(input()))

sort_li=merge_sort(li)

for num in sort_li:
    print(num)

