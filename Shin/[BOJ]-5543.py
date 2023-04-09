sum = 0
buger = []
drink = []
for i in range(5):
    num = int(input())
    if(i >= 3):
      drink.append(num)
    else:
        buger.append(num)
sum += min(buger)
sum += min(drink)
print(sum - 50)