import sys
input = sys.stdin.readline
n = int(input())
s = set(map(int, input().split()))
m = int(input())
c = list(map(int, input().split()))
visited = []
for i in c:
    if(i in s):
        visited.append(1)
    else:
        visited.append(0)


for i in visited:
    print(i, end = ' ')
