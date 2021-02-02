from _collections import deque

priorities = [2, 1, 3, 2]
location = 2
def solution():
    global location
    dq = deque(priorities)
    count = 0
    while True:
        max_value = max(dq)
        if location == 0 and max_value == dq[location]:
            count += 1
            break

        temp = dq.popleft()
        if max_value == temp:
            count += 1
        else:
            dq.append(temp)
        if location == 0:
            location = len(dq) - 1
        else:
            location -= 1
    return count
solution()