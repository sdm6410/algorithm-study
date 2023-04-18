n = int(input())
c_ = []
for _ in range(n):
    c = int(input())
    c_.append(c)
c_.sort(reverse=True)
for i in range(len(c_)):
    if(i % 3 == 2):
        c_[i] = 0
print(sum(c_))
