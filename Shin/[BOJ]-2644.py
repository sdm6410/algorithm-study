import sys
sys.setrecursionlimit(10**6)
# 노드 세팅
n = int(input())
p, q = map(int ,input().split())
family = [[] for i in range(n+1)]
visited = [False] * (n + 1)
m = int(input())
for i in range(m):
    x, y = map(int, input().split())
    family[x].append(y)
    family[y].append(x)
def dfs(start):
    for n in family[start]:
        if(visited[n] == False):
            visited[n] = visited[start] + 1
            dfs(n)

dfs(p)
print(visited[q] if visited[q] > 0 else -1)
