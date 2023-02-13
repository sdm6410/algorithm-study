sec = [300, 60, 10]
result = [0,0,0]
num = int(input())

def main(num):
    for s in range(len(sec)):
        count = 0
        count += num // sec[s]
        num %= sec[s]
        if (s == 2) & (num % sec[s] !=0):
            return False
        result[s] = count

if main(num) != False:
    for r in result:
        print(r, end =" ")
else:
    print(-1)
