n = int(input())
patten = input().split('*')
length = len(patten[0]) + len(patten[1])

for _ in range(n):
    file_name = input()
    if(length > len(file_name)):
        print('NE')
    else:
        if(patten[0] == file_name[:len(patten[0])] and patten[1] == file_name[-len(patten[1]):]):
            print('DA')
        else:
            print('NE')
