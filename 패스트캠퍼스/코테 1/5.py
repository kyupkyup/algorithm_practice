
def solution():
    N = 5
    D = 7
    x = [1, 1, 0, 1, 0, 1, 0]
    answer = int(1e9)
    p1 = 0
    p2 = 0

    while True:
        sum = 0
        if p2 > len(x):
            break

        for i in range(p1, p2):
            sum += x[i]
        if sum >= N:
            p1 += 1
            answer = min(answer, p2 - p1)
        else:
            p2 += 1

    if answer == int(1e9):
        print(-1)
        return
    print(answer)

    return
solution()