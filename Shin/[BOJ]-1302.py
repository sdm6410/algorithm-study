n = int(input())
dic = dict()
for _ in range(n):
    book = input()
    if(book in dic):
        dic[book] += 1
    else:
        dic[book] = 1

max_val = max(dic.values())
arr = []
for k,v in dic.items():
    if(max_val == v):
        arr.append(k)
arr.sort()
print(arr[0])
