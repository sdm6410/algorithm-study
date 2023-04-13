# 50점짜리
# S = list(input())
# q = int(input())
# for _ in range(q):
#     a, l, r = map(str,input().split())
#     count = 0
#     for i in S[int(l):int(r)+1]:
#         if(i == a):
#             count += 1
#     print(count)

import sys
input = sys.stdin.readline

cnt = [[0] * 26]
S = input()
for s in S:
    v = cnt[-1].copy()
    print(v)
    v[ord(s) % 97] += 1
    cnt.append(v)
for _ in range(int(input())):
    s, l, r = input().split()
    ind = ord(s) % 97
    print(cnt[int(r) + 1][ind] - cnt[int(l)][ind])
