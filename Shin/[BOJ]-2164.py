from collections import deque
n = int(input())
ex = [i for i in range(1,n+1)]

dq = deque()
dq.extend(ex)
while(len(dq) > 1):
    dq.popleft()
    dq.append(dq.popleft())

print(dq.pop())
