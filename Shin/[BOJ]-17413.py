s = list(input())
flag = False
word = ''
result = ''
for i in s:
    # 뒤집어서 < 만나기 전
    if(flag == False):
        if(i == '<'):
            flag = True
            word = word + i
        elif(i == ' '):
            word = word + i
            result = result + word
            word = ''
        else:
            word = i + word
    else:
        word = word + i
        if(i == '>'):
            flag = False
            result = result + word
            word =''
print(result + word)
