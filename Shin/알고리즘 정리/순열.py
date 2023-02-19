'''
1 2
1 3
2 1
2 3
3 1
3 2

1 2 != 2 1
'''

# 1. DFS를 이용
# 2. 체크리스트 이용
# 순열 암기

def DFS(L):
    # 종료 조건
    if(L == r):
        print(result)
    else:
        for i in range(len(n)):
            if(checklist[i] == 0):
                result[L] = n[i]
                checklist[i] = 1
                DFS(L+1)
                checklist[i] = 0

if __name__ == '__main__':
    n = [1,2,3]
    r = 2

    result = [0] * r
    checklist = [0] * len(n)

    DFS(0)