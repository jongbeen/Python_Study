N,K = list(map(int,input().split()))
coins = [0]*N
for i in range(N):
    coins[i] = int(input())

count=0
ptr = len(coins)-1
while K !=0:
    if K//coins[ptr] != 0:
        count += K//coins[ptr]
        K%=coins[ptr]
    ptr-=1
print(count)
