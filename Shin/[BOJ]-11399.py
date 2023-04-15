n = int(input())
sum = []
total = 0
P = list(map(int, input().split()))
P.sort()
sum.append(P[0])
for i in range(1,len(P)):
    sum.append(P[i] + sum[i-1])
for i in sum:
    total += i
print(total)