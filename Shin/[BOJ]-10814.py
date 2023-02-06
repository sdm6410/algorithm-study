
N = int(input())
arr = []
for _ in range(N):
    x, y = input().split()
    x = int(x)
    arr.append([x,y])
arr.sort(key= lambda x:x[0])
for i, j in arr:
    print(i, j)