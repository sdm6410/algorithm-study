from itertools import combinations
num_list = []
for _ in range(9):
    num = int(input())
    num_list.append(num)
for i in combinations(num_list,7):
    if(sum(i) == 100):
        for i_ in i:
            print(i_)
        break
