n, k=map(int, input().split())

a=list(map(int, input().split()))
tmp=1

def choco(list, cnt, day, tmp):
    if list[0]*n==sum(list):
        print(cnt, day)
        return
    if list[k+tmp-1]!=list[tmp-1]:
        cnt+=(list[k+tmp-1]-list[tmp-1])
        list[k+tmp-1]=list[tmp-1]
        day+=1
        list.sort()
    else:
        tmp+=1
    choco(list, cnt, day, tmp)

choco(a,0, 0, tmp)