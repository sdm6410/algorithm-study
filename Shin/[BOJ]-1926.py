import sys
sys.setrecursionlimit(10**6)
n, m = map(int, input().split())

space = []
for _ in range(n):
    space.append(list(map(int,input().split())))
ans =0
cnt = 0
tot_cnt = 0
def dfs(x, y):
    global cnt
    if(x <= -1 or x>=n or y<=-1 or y>= m):
        return False
    if(space[x][y] == 1):
        cnt += 1
        space[x][y] = 0
        # 상하좌우 재귀 호출
        dfs(x-1, y)
        dfs(x, y+1)
        dfs(x+1, y)
        dfs(x, y-1)
        return True
    return False

for i in range(n):
    for j in range(m):
        if(dfs(i, j) == True):
            tot_cnt += 1
            ans = max(cnt, ans)
            cnt = 0
print(tot_cnt)
print(ans)
