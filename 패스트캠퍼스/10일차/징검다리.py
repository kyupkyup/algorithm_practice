def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)
    rocks.insert(0, 0)

    left, right = 0, distance
    answer = -1

    while left <= right:
        mid = (left + right) // 2
        count = 0
        j = 0
        i = j + 1
        while i < len(rocks):
            if rocks[i] - rocks[j] < mid:
                i += 1
                count += 1
                continue
            j = i
            i += 1
        if count <= n:
            answer = max(answer, mid)
            left = mid + 1
        else:
            right = mid - 1

    return answer

distance = 25
rocks = [0, 2, 14, 11, 21, 17, distance]
n = 2
print(solution(distance, rocks, n))
