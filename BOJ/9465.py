t=int(input())
for _ in range(t):
    n=int(input())
    s=[]
    for _ in range(2):
        s.append(list(map(int, input().split())))
    s.append([0]*n)
    
    for i in range(1, n):
        s[0][i]+=max(s[1][i-1], s[2][i-1])
        s[1][i]+=max(s[0][i-1], s[2][i-1])
        s[2][i]+=max(s[0][i-1], s[1][i-1], s[2][i-1])
    print(max(s[0][n-1], s[1][n-1], s[2][n-1]))