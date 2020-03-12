
P = ""
newline = "\n"
T = input()
T = int(T)

while T>0:
    T -=1;
    R, test = input().split()
    R = int(R)
    
    for st in test:
        for i in range(0,R):
            P+=st
    P+=newline
print(P)
