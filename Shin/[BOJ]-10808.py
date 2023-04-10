word = list(input())
dic = {}
for i in range(97, 123):
    dic[chr(i)] = 0
for i in word:
    dic[i] += 1
for i in dic.values():
    print(i, end = ' ')
