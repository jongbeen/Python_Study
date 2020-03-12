
def dyn(n):
    ans = [0 for _ in range(n+1)]
    for i in range(n+1):
        if i<=2:
            ans[i] = i
        elif i==3:
            ans[i] = 4
        else :
            ans[i] = ans[i-1]+ans[i-2]+ans[i-3]
    
    return ans[n]

T = int(input())
ANS = []
while T>0:
    T-=1
    N = int(input())
    ANS.append(dyn(N))
for _ in range(len(ANS)):
    print(ANS[_])
