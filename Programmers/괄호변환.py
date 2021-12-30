from collections import deque
def balance(s):
    cnt_1, cnt_2=0, 0
    for i in range(len(s)):
        if s[i]=='(':
            cnt_1+=1
        else:
            cnt_2+=1
        if cnt_1==cnt_2:
            return i
    
def correct(s):
    q=deque()
    for i in range(len(s)):
        if s[i]=='(':
            q.append(s[i])
        else:
            if len(q)==0:
                return False
            else:
                q.pop()
    if len(q)==0:
        return True
    else:
        return False

def make_str(s):
    result=''
    if len(s)==0:
        return result
    if correct(s):
        return s
    
    while True:
        idx=balance(s)
        u=s[:idx+1]
        v=s[idx+1:]
        if correct(u):
            s=v
            result+=u
        else:
            result+='('
            result+=make_str(v)
            result+=')'
            for i in range(1, len(u)-1):
                if u[i]=='(':
                    result+=')'
                else:
                    result+='('
            return result
            
        if len(v)==0:
            break

    return result
            
def solution(p):
    answer = make_str(p)

    return answer