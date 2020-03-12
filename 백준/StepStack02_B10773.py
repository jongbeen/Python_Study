Num = list()

K = int(input())

for _ in range(K):
    N = int(input())
    if N==0:
        Num.pop()
    else:
        Num.append(N)

sum=0
for i in range(len(Num)):
    sum+=Num[i]
print(sum)
