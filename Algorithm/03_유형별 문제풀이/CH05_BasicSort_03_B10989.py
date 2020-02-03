import sys

N = int(sys.stdin.readline())
array = [0] * 10001

for _ in range(N):
    data = int(sys.stdin.readline())
    array[data] +=1

for i in range(N):
    if array[i] != 0:
        for j in range(array[i]):
            print(i)
