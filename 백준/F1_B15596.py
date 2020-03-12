def solve(a):
    ans = 0
    for i in range(0,len(a)):
        ans += a[i]
    return ans

a = [1,2,3,4,5]
print(solve(a))
