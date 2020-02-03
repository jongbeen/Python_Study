n = int(input())
num = [4,3,6,8,7,5,2,1]
mystack = []
result = []
count = 1
for i in range(1, n+1):
    data = int(input())
    while count <= data:
        stack.append(count)
        count +=1
        result.append('+')
    if stack[-1] == data:
        stack.pop()
        result.append('-')
    else:
        print('no')
        exit(0)

print("\n".join(result))
