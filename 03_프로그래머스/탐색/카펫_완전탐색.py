import math
def solution(brown, yellow):
    y = int(math.sqrt(yellow)) + 1
    suspect = []
    for i in range(1,y):
        if yellow % i == 0:
            row = yellow // i
            if row >= i:
                suspect.append((row,i))
    answer = []
    print(suspect)
    for sus in suspect:
        row, col = sus
        if (row + 2) * (col + 2) == brown + yellow:
            answer = [row+2,col+2]
            break
    return answer
print(solution(10,2))
print(solution(8,1))
print(solution(24,24))