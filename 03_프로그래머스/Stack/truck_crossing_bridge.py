def solution(bridge_length, weight, truck_weights):
    time = 0
    q = [0] * bridge_length

    while q:
        time += 1
        q.pop(0)
        if truck_weights:
            if sum(q) + truck_weights[0] <= weight:
                q.append(truck_weights.pop(0))
            else:
                q.append(0)
    return time

# l, w, t_w = 2,10,[7,4,5,6]
l, w, t_w = 100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
print(solution(l,w,t_w))