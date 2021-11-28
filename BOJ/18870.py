n=int(input())
x=list(map(int, input().split()))

x_sort=list(set(x))
x_sort.sort()
x_sort_dic={x_sort[tmp]: tmp for tmp in range(len(x_sort))}
for i in x:
    print(x_sort_dic[i], end=' ')