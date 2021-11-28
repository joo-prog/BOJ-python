n=int(input())
sequence=list(map(int,input().split()))
sequence_sum=[sequence[0]]

for i in range(1, n):
    sequence_sum.append(max(sequence_sum[i-1]+sequence[i], sequence[i]))

print(max(sequence_sum))