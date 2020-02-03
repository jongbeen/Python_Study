# 이것도 되는데... 그냥 정답으로 제출하겠음
Pro = dict()
N = int(input())
for _ in range(N):
    Age, Name = input().split()
    Age = int(Age)
    Pro[Name] = Age
Pro = sorted(Pro.items(), key=lambda item:item[1])

for key,value in Pro:
    print(value," ",key)

