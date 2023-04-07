answer = ''
word = input()
for i in word:
    if(i.isupper()):
        answer += i.lower()
    elif(i.islower()):
        answer += i.upper()
print(answer)