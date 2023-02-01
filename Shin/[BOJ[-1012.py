import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
num = int(input())

def dfs(x, y,ground):
    ground[x][y] = 0
    ret = 0
    for(dx, dy) in [(1,0), (-1,0), (0,1), (0,-1)]:
        xx, yy = x+dx, y+dy
        if not (0 <= xx < N and 0 <= yy < M):
            continue
        if(ground[xx][yy]):
            ret += dfs(xx, yy,ground)
    return ret+1

for _ in range(num):
    M, N, K = map(int, input().split())
    res = []
    ground = [[0] * M for _ in range(N)]
    for _ in range(K):
        X, Y = map(int, input().split())
        ground[Y][X] = 1
    for i in range(N):
        for j in range(M):
            if(ground[i][j]):
                res.append(dfs(i, j,ground))
    res.sort()
    print(len(res))