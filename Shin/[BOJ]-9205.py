from collections import deque
import sys
input = sys.stdin.readline
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def distance(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)

def bfs(x, y):
    global end_x, end_y
    q = deque([[x,y]])
    visited = set()
    while(q):
        x, y = q.popleft()
        if(distance(x, y, end_x, end_y) <= 1000):
            return True
        for i in range(n):
            store_x, store_y = store[i]
            if(store_x, store_y) not in visited:
                if(distance(x,y, store_x, store_y) <= 1000):
                    visited.add((store_x, store_y))
                    q.append([store_x, store_y])
    return False



t = int(input())
for _ in range(t):
    # 편의점 갯수
    n = int(input())
    # 집 위치 n
    # n+2 락 페스티벌
    home_x, home_y = map(int,input().split())
    store = [list(map(int, input().split())) for _ in range(n)]
    end_x, end_y = map(int,input().split())
    check = bfs(home_x, home_y)
    print('happy' if check else 'sad')

