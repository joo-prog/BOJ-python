import sys
input=sys.stdin.readline

n=int(input())
cnt=0
for _ in range(n):
    word=input().strip()
    for i in range(0, len(word)-1):
        if word[i]==word[i+1]:
            continue
        elif word[i] in word[i+1:]:
            cnt+=1
            break
print(n-cnt)