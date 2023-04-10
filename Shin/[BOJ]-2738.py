n, m = map(int, input().split())
A = []
B = []
for _ in range(n):
    A.append(list(map(int, input().split())))
for _ in range(n):
    B.append(list(map(int,input().split())))
for i in range(len(A)):
    for j in range(len(A[0])):
        print(A[i][j] + B[i][j], end=' ')
    print()
