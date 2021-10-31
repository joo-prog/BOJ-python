student=[]

for _ in range(5):
    student.append(list(input()))

tmp1=['.', 'o', 'm', 'l', 'n']
tmp2=['o', 'w', 'l', 'n', '.']
tmp3=['.', '.', 'o', 'L', 'n']

t=list(map(list, zip(*student)))

tmp=[]
for i in range(len(student[0])):
    if t[i]==tmp3:
        tmp.append(tmp3)

    elif t[i]==tmp1:
        tmp.append(tmp2)
    elif t[i]==tmp2:
        tmp.append(tmp1)

t_tmp=list(map(list, zip(*tmp)))

for i in range(5):
    for j in range(len(student[0])):
        print(t_tmp[i][j], end='')
    print()