num = []
for _ in range(9):
    num.append(list(map(int, input().split())))
max = -1
X = 0
Y = 0
for i in range(len(num)):
    for j in range(len(num[0])):
        if(max < num[i][j]):
            max = num[i][j]
            X = i + 1
            Y = j + 1

print(max)
print(X, Y)

