import sys
sys.setrecursionlimit(10**5)
n=int(input())
inorder=list(map(int, input().split()))
postorder=list(map(int, input().split()))

def dfs(in_start, in_end, post_start, post_end):
    if in_start>in_end and post_start>post_end:
        return
    root=postorder[post_end]
    print(root, end=" ")

    in_idx=inorder.index(root)
    left_cnt=in_idx-in_start
    right_cnt=in_end-in_idx

    dfs(in_start, in_start+left_cnt-1, post_start, post_start+left_cnt-1)
    dfs(in_end-right_cnt+1, in_end, post_end-right_cnt, post_end-1)

dfs(0, n-1, 0, n-1)