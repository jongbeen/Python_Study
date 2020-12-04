def solution(n):

    res = [[0] * n for _ in range(n)]
    x,y = -1, 0
    num = 1
    for i in range(n):
        for j in range(i,n):
            if i % 3 == 0:
                x += 1
                res[x][y] = num
            if i % 3 == 1:
                y += 1
                res[x][y] = num
            if i % 3 == 2:
                x -= 1
                y -= 1
                res[x][y] = num
            num += 1
    answer = []
    # print(res)
    for row in res:
        for data in row:
            if data != 0:
                answer.append(data)
    return answer
print(solution(4))