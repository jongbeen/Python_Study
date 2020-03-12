Time = int(input())
Wait = list(map(int, input().split()))
answer = 0
Wait.sort()

for i in range(Time):
    answer += Wait[i] * (Time-i)

print(answer)
