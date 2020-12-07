def find_first(arr,quad):
    temp = []
    for i in range(quad):
        temp.append(arr[i][:quad])
    return temp

def find_second(arr,quad):
    temp = []
    for i in range(quad):
        temp.append(arr[i][quad:])
    return temp

def find_third(arr,quad):
    temp = []
    for i in range(quad,len(arr)):
        temp.append(arr[i][:quad])
    return temp

def find_fourth(arr,quad):
    temp = []
    for i in range(quad,len(arr)):
        temp.append(arr[i][quad:])
    return temp

def balanced(arr):
    length = len(arr)
    standard = arr[0][0]
    result = True
    for i in range(length):
        for j in range(length):
            if arr[i][j] != standard:
                result = False
                break
    return result

def solution(arr):
    length = len(arr)
    answer = []
    if length == 1:
        return arr
    quad = length // 2
    first_arr = find_first(arr,quad)
    second_arr = find_second(arr,quad)
    third_arr = find_third(arr,quad)
    fourth_arr = find_fourth(arr,quad)

    if balanced(first_arr):
        answer.append(first_arr[0][0])
    else:
        solution(first_arr)
    if balanced(second_arr):
        answer.append(second_arr[0][0])
    else:
        solution(second_arr)
    if balanced(third_arr):
        answer.append(third_arr[0][0])
    else:
        solution(third_arr)
    if balanced(fourth_arr):
        answer.append(fourth_arr[0][0])
    else:
        solution(fourth_arr)
    print(answer)
    return answer


# print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]))
solution([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]])