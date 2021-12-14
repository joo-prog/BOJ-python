a, b, c=map(int, input().split())

def mul(tmp_b):
    if tmp_b==1:
        return a%c
    if tmp_b%2==1:
        tmp_result=mul(tmp_b//2)
        result=(tmp_result*tmp_result*a)%c
    else:
        tmp_result=mul(tmp_b//2)
        result=(tmp_result*tmp_result)%c
    return result

print(mul(b))