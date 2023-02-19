'''

1 2
1 3
2 3

3
'''
# 1. DFS 트리를 이용.
# 2. 다음 Depth에서의 시작값.
# 조합 암기

def DFS(L, BeginWith):
    # 종료 조건
    if(L == r):
        print(result)
    else:
        for i in range(BeginWith, len(n)):
            result[L] = n[i]
            DFS(L+1, i+1)


if __name__ == '__main__':
    n = [1,2,3]
    r = 2

    result = [0] * r
    DFS(0, 0) # 0 level, 0 BeginWith