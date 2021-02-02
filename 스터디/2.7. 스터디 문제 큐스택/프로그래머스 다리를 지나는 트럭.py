from collections import deque

bridge_length = 100
weight = 100
truck_weights = [10,10,10,10,10,10,10,10,10,10]

def solution():
    time = 1
    truck_weights_q = deque(truck_weights)
    truck_ing = deque([])
    time_list = deque([])

    while True:
        if not truck_ing and not truck_weights_q:
            break
        else:
            if truck_weights_q:
                if sum(truck_ing) + truck_weights_q[0] <= weight:
                    truck_ing.append(truck_weights_q.popleft())
                    time_list.append(bridge_length)
            for i in range(len(time_list)):
                time_list[i] -= 1
            if time_list[0] == 0:
                time_list.popleft()
                truck_ing.popleft()
        time += 1

    return time

solution()