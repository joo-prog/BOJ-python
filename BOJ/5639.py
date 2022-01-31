import sys
sys.setrecursionlimit(10 ** 9)
input=sys.stdin.readline

def postorder(start, end, tree):
    if start > end:
        return
    root=tree[start]
    mid=end+1
    for i in range(1, end-start+1):
        if tree[start+i]>root:
            mid=start+i
            break
    postorder(start+1, mid-1, tree)
    postorder(mid, end, tree)
    print(root)

li=[]
while True:
    try:
        li.append(int(input()))
    except:
        break

postorder(0, len(li)-1, li)