# B로 먼저 색칠
n = int(input())
color = input()
B_cnt = 0
for c in color.split("B"):
    if c != '':
        B_cnt += 1

# R로 먼저 색칠
R_cnt = 0
for c in color.split("R"):
    if c != '':
        R_cnt += 1

# 순서대로 색칠
cnt = 0
for i in range(len(color) - 1):
    if color[i] != color[i + 1]:
        cnt += 1

print(min(B_cnt + 1, R_cnt + 1, cnt + 1))