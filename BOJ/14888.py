n=int(input())
li=list(map(int, input().split()))
add, minus, mul, div=map(int, input().split())

max_res=-1e9
min_res=1e9

def dfs(res, tmp_n, add, minus, mul, div):
    global max_res, min_res
    if tmp_n==n:
        max_res=max(res, max_res)
        min_res=min(res, min_res)
        return

    if add!=0:
        dfs(res+li[tmp_n], tmp_n+1, add-1, minus, mul, div)
    if minus!=0:
        dfs(res-li[tmp_n], tmp_n+1, add, minus-1, mul, div)
    if mul!=0:
        dfs(res*li[tmp_n], tmp_n+1, add, minus, mul-1, div)
    if div!=0:
        dfs(int(res//li[tmp_n]), tmp_n+1, add, minus, mul, div-1)

dfs(li[0], 1, add, minus, mul, div)
print(max_res)
print(min_res)