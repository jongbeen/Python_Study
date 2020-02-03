N = int(input())
Ray = []
for _ in range(N):
    X,Y = list(map(int,input().split()))
    Ray.append((X,Y))
    
Ray.sort()
for i in Ray:
    print(i[0],i[1])
