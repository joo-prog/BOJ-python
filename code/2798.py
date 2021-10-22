n, m=map(int, input().split())
card=list(map(int, input().split()))

min_diff=300000

for i in range(0, len(card)-2):
    for j in range(i+1, len(card)-1):
        for k in range(j+1, len(card)):
            sum=card[i]+card[j]+card[k]
            diff=m-sum
            if (diff>=0) & (diff<min_diff):
                min_diff=diff
                max_sum=sum

print(max_sum)
