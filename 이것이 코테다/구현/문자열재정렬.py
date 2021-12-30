s=list(input().strip())
s.sort()

sum=0
for i in range(len(s)):
    if 'A'<=s[i]<='Z':
        print(s[i], end='')
    else:
        sum+=int(s[i])
print(sum)