n = int(input())
for _ in range(n):
    T = int(input())
    result = []
    for i in range(len(bin(T)[2:])):
        if(bin(T)[2:][i] == '1'):
            result.append(len(bin(T)[2:]) - i-1)
    result.sort()
    for i in result:
        print(i, end= ' ')