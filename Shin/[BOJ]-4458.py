n = int(input())
for _ in range(n):
    sentance = input()
    sentance = list(sentance)
    for i in range(len(sentance)):
        if(i == 0):
            print(sentance[i].upper(), end='')
        else:
            print(sentance[i], end='')
    print()