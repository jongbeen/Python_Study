import heapq

N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
Sum = 0

heapq.heapify(B)
A.sort(reverse=True)

for i in range(len(A)):
    b = heapq.heappop(B)
    Sum += A[i]*b
print(Sum)
