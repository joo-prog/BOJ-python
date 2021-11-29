def solution(n):
    answer = 0
    fib=[]
    for i in range(0, n+1):
        if i==0 or i==1:
            fib.append(i)
        else:
            fib.append(fib[i-1]+fib[i-2])
            
    answer=fib[n]%1234567
    return answer