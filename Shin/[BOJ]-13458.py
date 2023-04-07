import math

answer = 0
n = int(input())
student = list(map(int, input().split()))
total, sub = map(int, input().split())
for i in student:
    if(i > 0):
        i -= total
        answer += 1
        answer = answer + math.ceil(i / sub)



print(answer)