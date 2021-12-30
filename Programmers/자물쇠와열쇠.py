def rotation(matrix, n):
    result=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[j][n-1-i]=matrix[i][j]
    return result

def solution(key, lock):
    m=len(key)
    n=len(lock)
    
    lock_result=[[0]*(n*3) for _ in range(n*3)]
    for i in range(n):
        for j in range(n):
            lock_result[n+i][n+j]=lock[i][j]
    
    for i in range(n*2):
        for j in range(n*2):
            for r in range(4):
                key=rotation(key, m)
                for l in range(m):
                    for k in range(m):
                        lock_result[i+l][j+k]+=key[l][k]
                cnt=0
                for l in range(n, n*2):
                    for k in range(n, n*2):
                        if lock_result[l][k]==1:
                            cnt+=1
                if cnt==n*n:
                    return True
                
                for l in range(m):
                    for k in range(m):
                        lock_result[i+l][j+k]-=key[l][k]
                
    return False