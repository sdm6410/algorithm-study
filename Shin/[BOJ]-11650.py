import sys
input = sys.stdin.readline
N = int(input())
arr = []
for _ in range(N):
    x, y = map(int, input().split())
    arr.append([x,y])
arr = sorted(arr)

for i, j in arr:
    print(i, j)