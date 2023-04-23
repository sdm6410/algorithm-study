T = int(input())
for _ in range(T):
    J, N = map(int,input().split())
    canny = []
    count = 0
    for _ in range(N):
        R, C = map(int, input().split())
        canny.append(R*C)
    canny.sort(reverse=True)
    for i in canny:
        J -= i
        count += 1
        if(J <= 0):
            print(count)
            break
