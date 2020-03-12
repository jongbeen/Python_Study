A,B = input().split()
A = list(A)
B = list(B)

A.reverse()
B.reverse()
a=""
b=""

for i in range(len(A)):
    a += str(A[i])
    b += str(B[i])
A = int(a)
B = int(b)
if A<B:
    print(B)
else:
    print(A)
