def solution(s):
    answer = 1000
    
    for i in range(1, len(s)//2+2):
        cnt=1
        string=''
        tmp=s[:i]
        for j in range(i, len(s)+i, i):
            if s[j:j+i]==tmp:
                cnt+=1
            else:
                if cnt==1:
                    string+=tmp
                else:
                    string+=(str(cnt)+tmp)
                tmp=s[j:j+i]
                cnt=1
        answer=min(answer, len(string))
    return answer