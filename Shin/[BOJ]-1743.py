# 좌표 세팅완료
import sys
sys.setrecursionlimit(10**6)
n, m, k = map(int, input().split())
cnt = 0
ans = 0
space = [[0] * m for i in range(n)]
for _ in range(k):
    x, y = map(int, input().split())
    space[x-1][y-1] = 1

# dfs 함수
def dfs(x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    global cnt
    if(x <= -1 or x >= n or y <= -1 or y >= m):
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if(space[x][y] == 1):
        # 해당 노드 방문 처리
        cnt += 1
        space[x][y] = 0

        # 상하좌우 재귀 호출
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

for i in range(n):
    for j in range(m):
        if(dfs(i, j) == True):
            ans = max(cnt, ans)
            cnt = 0
print(ans)

