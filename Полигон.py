for _ in range(int(input())):
    n = int(input())
    A = [input() for _ in range(n)]
    if any(A[i][j] == '1' and A[i][j + 1] == A[i + 1][j] == '0'
           for i in range(n - 1) for j in range(n - 1)):
        print('NO')
    else:
        print('YES')
