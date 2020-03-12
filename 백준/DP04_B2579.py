
# 1.현재값 + 현재값-2 까지의 합 VS 2.최근2개 값 + 그전까지의 합
# 현(밟)+전(밟X) +전전(최대)

# 2.는 2칸 연속 걸었다는 가정
# 현(밟),전(밟),+전전(밟X)+전전전(밟)
# 이 두가지중 더 큰 값을 구하면 되는 문제

stairs = int(input())
N = stairs
point = []
ans = [0 for _ in range(N)]

while(stairs>0):
    stairs-=1
    point.append(int(input()))

for i in range(N):
    if i==0:
        ans[i] = point[i]
    elif i==1:
        ans[i] = point[i]+point[i-1]
    elif i==2:
        ans[i] = max(point[i]+point[i-2],point[i]+point[i-1])
    else :
        ans[i] = max(point[i]+ans[i-2],point[i]+point[i-1]+ans[i-3])

print(ans[-1])
