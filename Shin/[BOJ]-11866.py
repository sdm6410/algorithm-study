n,k = map(int, input().split())

array = [i for i in range(1,n+1)]
ans = []
pt = 0
for _ in range(n):
    pt += k - 1
    pt %= len(array)
    ans.append(array.pop(pt))

print(f"<{', '.join(map(str, ans))}>")