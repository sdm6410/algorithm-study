N, L = map(int, input().split())
h = list(map(int, input().split()))
visited = [L + i for i in range(N+1)]
h.sort()
for i in h:
    if(i > L):
        break
    L += 1
print(L)
