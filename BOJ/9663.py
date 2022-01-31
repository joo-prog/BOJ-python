n=int(input())
result=0
visited=[0]*n
board=[0]*n

def check(x):
    for i in range(x):
        if abs(board[x]-board[i])==x-i:
            return False
    return True

def queen(x):
    global result
    if x==n:
        result+=1
        return
    for i in range(n):
        if visited[i]==1:
            continue
        board[x]=i
        if check(x):
            visited[i]=1
            queen(x+1)
            visited[i]=0
queen(0)
print(result)