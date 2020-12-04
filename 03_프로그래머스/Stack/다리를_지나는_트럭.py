def solution(bridge_length, weight, truck_weights):
    time = 0
    stack = [0] * bridge_length

    while stack:
        time += 1
        stack.pop(0)
        if truck_weights:
            if sum(stack) + truck_weights[0] <= weight:
                item = truck_weights.pop(0)
                stack.append(item)
            else:
                stack.append(0)
    return time

# l, w, t_w = 2,10,[7,4,5,6]
l, w, t_w = 100,100,[10,10,10,10,10,10,10,10,10,10]
print(solution(l,w,t_w))