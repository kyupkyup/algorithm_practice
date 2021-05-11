
def solution():

    N = 4
    fry = [2, 2, 1, 3]
    clean = [2, 4, 3, 2]
    chickens = 2
    time = []
    start = 0
    answer = 100000000
    for i in range(len(fry)):
        time.append(fry[i] + clean[i])
    end = max(time) * chickens

    while start <= end:
        mid = (start + end) // 2
        sum = 0
        for i in time:
            sum += mid // i

        if sum > chickens:
            end = mid - 1
        elif sum < chickens:
            start = mid + 1
        elif sum == chickens:
            end -= 1
            answer = min(answer, mid)

    print(answer)


solution()