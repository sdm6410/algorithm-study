n, w = map(int, input().split())
s = []
for _ in range(n):
    s.append(int(input()))
m = s[0]
coin = 0
for i in s:
    if(m > i):
        m = i
    elif(m < i):
        coin = w // m
        w = w - m * coin
        w = w + coin * i
        m = i
print(w)