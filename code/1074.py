N, r, c=map(int, input().split())

def visit(n, row, col):
    if n==1:
        if (row==0)&(col==0):
            return 1
        elif (row==0)&(col==1):
            return 2
        elif (row==1)&(col==0):
            return 3
        else:
            return 4

    if (row<2**(n-1))&(col<2**(n-1)):
        return visit(n-1, row, col)
    elif (row<2**(n-1))&(col>=2**(n-1)):
        return 2**(2*n-2)+visit(n-1, row, col-2**(n-1))
    elif (row>=2**(n-1))&(col<2**(n-1)):
        return (2**(2*n-1))+visit(n-1, row-2**(n-1), col)
    else:
        return (2**(2*n-2))*3+visit(n-1, row-2**(n-1), col-2**(n-1))

print(visit(N, r, c)-1)