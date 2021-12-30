n=input().strip()
sum_left=0
sum_right=0
for i in range(len(n)//2):
    sum_left+=int(n[i])
for i in range(len(n)//2, len(n)):
    sum_right+=int(n[i])
if sum_left==sum_right:
    print('LUCKY')
else:
    print('READY')