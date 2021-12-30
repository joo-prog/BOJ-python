n=int(input())
li=list(map(int, input().split()))
li.sort()
target=1
for i in li:
    if target<i:
        break
    target+=i
print(target)