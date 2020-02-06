
N, M = list(map(int, input().split()))
card = list(map(int,input().split()))
result = 0
for i in range(0,len(card)):
    for j in range(i+1,len(card)):
        for k in range(j+1,len(card)):
            sum_value = card[i]+card[j]+card[k]
            if sum_value<=M:
                # 둘중 더 큰값 리턴
                result = max(result,sum_value)
print(result)
