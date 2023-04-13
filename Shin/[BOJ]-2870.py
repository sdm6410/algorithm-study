m = int(input())
num = []
for _ in range(m):
    n = list(input())
    answer = ''
    for i in n:
        if(i.isalpha()):
            if(len(answer) != 0):
                num.append(int(answer))
                answer = ''
        else:
            answer += i
    if(len(answer) != 0):
        num.append(int(answer))

for i in sorted(num):
    print(i)
