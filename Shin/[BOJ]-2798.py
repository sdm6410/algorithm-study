n, m = map(int, input().split())
card = list(map(int, input().split()))
answer = []
def dfs(L, BeginWith):
    # 종료조건
    if(L == r):
        if(sum(result) <= m):
            answer.append(sum(result))
    else:
        for i in range(BeginWith, len(card)):
            result[L] = card[i]
            dfs(L+1, i+1)
r = 3
result = [0] * r
dfs(0, 0)
print(max(answer))