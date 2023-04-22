def mix_drink(a,b):
    xa = a + (b / 2)
    xb = b + (a / 2)
    return max(xa, xb)

n = int(input())
drink = list(map(int, input().split()))
drink.sort()
while(len(drink) != 1):
    a = drink.pop()
    b = drink.pop()
    c = mix_drink(a, b)
    drink.append(c)
print(drink[0])