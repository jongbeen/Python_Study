def quicksort(data):
    if len(data)<=1:
        return data
    pivot = data[0]
    left = [item for item in data[1:] if pivot > item]
    right = [item for item in data[1:] if pivot <=item]
    
    return quicksort(left)+[pivot]+quicksort(right)

N = int(input())
ANS = [0] * N
for i in range(N):
    ANS[i] = int(input())

ANS = quicksort(ANS)

for i in range(len(ANS)):
    print(ANS[i])
