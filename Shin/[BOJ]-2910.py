from collections import Counter
n, c = map(int, input().split())
num = list(map(int, input().split()))
num_counter = Counter(num).most_common()

for key, value in num_counter:
    for i in range(value):
        print(key, end = ' ')
